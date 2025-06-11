# Feature: Listado de Cursos

## Descripción
Feature completa para mostrar una lista de cursos disponibles en la aplicación PlatziFlixAndroid, implementada siguiendo la arquitectura CLEAR y las mejores prácticas de desarrollo Android.

## Arquitectura

### Estructura del proyecto
```
app/src/main/java/com/espaciotiago/platziflixandroid/
├── data/
│   ├── entities/
│   │   └── CourseDTO.kt                    # Data Transfer Object
│   ├── mappers/
│   │   └── CourseMapper.kt                 # Mapper DTO → Domain Model
│   ├── network/
│   │   ├── ApiService.kt                   # Retrofit API interface
│   │   └── NetworkModule.kt                # Network configuration
│   └── repositories/
│       ├── RemoteCourseRepository.kt       # Remote data implementation
│       └── MockCourseRepository.kt         # Mock data for development
├── domain/
│   ├── models/
│   │   └── Course.kt                       # Domain model
│   └── repositories/
│       └── CourseRepository.kt             # Repository interface
├── presentation/
│   └── courses/
│       ├── components/
│       │   ├── CourseCard.kt               # Course item component
│       │   ├── ErrorMessage.kt             # Error display component
│       │   └── LoadingIndicator.kt         # Loading component
│       ├── screen/
│       │   └── CourseListScreen.kt         # Main screen
│       ├── state/
│       │   └── CourseListUiState.kt        # UI State & Events
│       └── viewmodel/
│           └── CourseListViewModel.kt      # Business logic
├── di/
│   └── AppModule.kt                        # Dependency injection
└── ui/theme/
    ├── Color.kt                            # Color palette
    ├── Spacing.kt                          # Design system
    └── Theme.kt                            # Material 3 theme
```

## Tecnologías Utilizadas

### Core
- **Kotlin**: Lenguaje principal
- **Jetpack Compose**: UI moderna y declarativa
- **Material 3**: Sistema de diseño

### Arquitectura
- **MVVM + MVI**: Patrón de presentación
- **Clean Architecture**: Separación de responsabilidades
- **Repository Pattern**: Abstracción de fuentes de datos

### Networking
- **Retrofit**: Cliente HTTP
- **OkHttp**: Interceptores y logging
- **Gson**: Serialización JSON

### UI/UX
- **Coil**: Carga de imágenes
- **Pull-to-Refresh**: Actualización manual
- **State Management**: Flujos reactivos con StateFlow

### Testing
- **JUnit**: Testing unitario
- **Coroutines Test**: Testing asíncrono
- **Mockito**: Mock objects

## Características Implementadas

### ✅ Funcionalidades Core
- [x] Lista de cursos con diseño responsive
- [x] Carga asíncrona de datos
- [x] Manejo de estados (Loading, Success, Error, Empty)
- [x] Pull-to-refresh
- [x] Retry en caso de error
- [x] Carga de imágenes optimizada

### ✅ UI/UX
- [x] Diseño Material 3
- [x] Tema claro y oscuro
- [x] Animaciones fluidas
- [x] Componentes reutilizables
- [x] Estados de carga y error informativos

### ✅ Arquitectura
- [x] Separación de capas
- [x] Inyección de dependencias
- [x] Mappers para transformación de datos
- [x] Repository pattern
- [x] ViewModels con StateFlow

### ✅ Testing
- [x] Tests unitarios para ViewModel
- [x] Mock repositories para desarrollo
- [x] Test de estados UI
- [x] Test de manejo de errores

## Configuración

### 1. Dependencias
Las dependencias están configuradas en `app/build.gradle.kts`:

```kotlin
// HTTP client
implementation("com.squareup.retrofit2:retrofit:2.9.0")
implementation("com.squareup.retrofit2:converter-gson:2.9.0")

// Image loading
implementation("io.coil-kt:coil-compose:2.5.0")

// ViewModel
implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.7.0")
```

### 2. Permisos
En `AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### 3. Configuración de red
En `NetworkModule.kt` se puede configurar la URL base:
```kotlin
private const val BASE_URL = "http://localhost:8000/"
```

### 4. Modo desarrollo
En `AppModule.kt` se puede alternar entre datos mock y API real:
```kotlin
private const val USE_MOCK_DATA = true // Set to false to use real API
```

## Uso

### Integración en MainActivity
```kotlin
@Composable
fun PlatziFlixApp() {
    val courseListViewModel = viewModel<CourseListViewModel> {
        AppModule.provideCourseListViewModel()
    }
    
    CourseListScreen(
        viewModel = courseListViewModel,
        onCourseClick = { course ->
            // Navigate to course detail
        }
    )
}
```

### Estados manejados
- **Loading**: Indicador de carga inicial
- **Success**: Lista de cursos
- **Error**: Mensaje de error con botón de retry
- **Empty**: Mensaje cuando no hay cursos
- **Refreshing**: Pull-to-refresh activo

## API Contract

### Endpoint
```
GET /courses
```

### Response
```json
[
  {
    "id": 1,
    "name": "Curso de Kotlin",
    "description": "Aprende Kotlin desde cero...",
    "thumbnail": "https://example.com/image.png",
    "slug": "curso-de-kotlin",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "deleted_at": null,
    "teacher_id": [1, 2]
  }
]
```

## Testing

### Ejecutar tests
```bash
./gradlew test
```

### Estructura de tests
- **Unit Tests**: `app/src/test/`
- **Integration Tests**: `app/src/androidTest/`

### Casos de prueba cubiertos
- Estados iniciales del ViewModel
- Carga exitosa de cursos
- Manejo de errores de red
- Funcionalidad de refresh
- Limpieza de errores

## Próximas mejoras

### 🔄 Pendientes
- [ ] Caché local con Room
- [ ] Paginación infinita
- [ ] Filtros y búsqueda
- [ ] Navegación a detalle de curso
- [ ] Favoritos
- [ ] Compartir cursos
- [ ] Modo offline

### 🚀 Optimizaciones
- [ ] Lazy loading de imágenes
- [ ] Preload de contenido
- [ ] Métricas de rendimiento
- [ ] A/B testing para UI

## Troubleshooting

### Problemas comunes

1. **Error de conexión**
   - Verificar permisos de internet
   - Configurar network security config para HTTP (desarrollo)

2. **Imágenes no cargan**
   - Verificar URLs de thumbnails
   - Comprobar conectividad de red

3. **Tests fallan**
   - Verificar dependencias de testing
   - Configurar TestDispatcher correctamente

## Contribución

### Estándares de código
- Seguir convenciones de Kotlin
- Documentar funciones públicas
- Mantener cobertura de tests > 80%
- Usar nombres descriptivos en inglés

### Pull Request
1. Crear branch desde `develop`
2. Implementar feature
3. Agregar tests
4. Actualizar documentación
5. Hacer PR con descripción detallada

---

**Desarrollado con ❤️ para PlatziFlixAndroid** 