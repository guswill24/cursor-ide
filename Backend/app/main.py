from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Annotated
from app.core.config import Settings, get_settings
from app.db.base import engine, get_db
from app.services.course_service import CourseService

app = FastAPI()


def configure_app(settings: Annotated[Settings, Depends(get_settings)]) -> None:
    """
    Configure FastAPI app with settings
    """
    app.title = settings.project_name
    app.version = settings.version


# Configure app on startup
@app.on_event("startup")
async def startup_event():
    settings = get_settings()
    configure_app(settings)


def get_course_service(db: Session = Depends(get_db)) -> CourseService:
    """
    Dependency to get CourseService instance
    """
    return CourseService(db)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Bienvenido a Platziflix API"}


@app.get("/health")
def health(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str | bool | int]:
    """
    Health check endpoint that verifies:
    - Service status
    - Database connectivity
    """
    health_status = {
        "status": "ok",
        "service": settings.project_name,
        "version": settings.version,
        "database": False,
    }

    # Check database connectivity and verify migration
    try:
        with engine.connect() as connection:
            # Execute COUNT on courses table to verify migration was executed
            result = connection.execute(text("SELECT COUNT(*) FROM courses"))
            row = result.fetchone()
            if row:
                count = row[0]
                health_status["database"] = True
                health_status["courses_count"] = count
            else:
                health_status["database"] = True
                health_status["courses_count"] = 0
    except Exception as e:
        health_status["status"] = "degraded"
        health_status["database_error"] = str(e)

    return health_status


@app.get("/courses")
def get_courses(course_service: CourseService = Depends(get_course_service)) -> list:
    """
    Get all courses.
    Returns a list of courses with basic information: id, name, description, thumbnail, slug
    """
    return course_service.get_all_courses()


@app.get("/courses/{slug}")
def get_course_by_slug(slug: str, course_service: CourseService = Depends(get_course_service)) -> dict:
    """
    Get course details by slug.
    Returns course information including teachers and classes.
    """
    course = course_service.get_course_by_slug(slug)
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
