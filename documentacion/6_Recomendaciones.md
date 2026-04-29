# CAPÍTULO 6: RECOMENDACIONES

A partir de las conclusiones extraídas del modelado predictivo de rezago escolar y la estructuración del ecosistema de datos de la institución primaria de Cochabamba, se proponen las siguientes recomendaciones de alcance operativo y metodológico, orientadas a consolidar la alerta temprana en el centro educativo:

## 6.1 Recomendaciones Metodológicas y de Toma de Datos

**1. Transición hacia captura y modelado trimestral:**
La recomendación de mayor impacto para el futuro es migrar la granularidad de los datos. **Se recomienda enfáticamente transicionar hacia un registro y análisis trimestral o bimensual** de las calificaciones, en lugar de depender exclusivamente de los promedios anualizados. Modelar sobre los primeros trimestres del año permitirá que el Bosque Aleatorio actúe con inmediatez, identificando patrones de declive temprano y permitiendo la intervención pedagógica meses antes del fracaso a final de gestión.

**2. Rediseño analítico docente:**
Se recomienda institucionalizar el uso del Dashboard interactivo (*Streamlit*) como herramienta de consulta obligatoria en los consejos de profesores. Al clasificar a los estudiantes en clústeres de riesgo (Alto, Medio, Bajo), la dirección y psicopedagogía deben coordinar con los tutores para ejecutar intervenciones extracurriculares focalizadas, reforzando especialmente materias críticas como Matemáticas y Comunicación y Lenguajes.

## 6.2 Mantenimiento Técnico y Consideraciones a Futuro

**3. Mantenimiento matemático, reentrenamiento y ética:**
Se debe tener presente que los resultados obtenidos son producto de un análisis que abarca estrictamente el comportamiento histórico entre 2022 y 2024, sujeto a hipótesis y condiciones socio-educativas de ese periodo. Por lo tanto, estos resultados deben irse calibrando en el tiempo; **se recomienda imperativamente un reentrenamiento manual del modelo** al concluir cada año, añadiendo los nuevos registros al *dataset*. Además, la etiqueta de "Riesgo de Rezago" debe ser estrictamente confidencial, existiendo solo para apoyar al menor, sin estigmatizarlo públicamente.

**4. Extensión modular del proyecto:**
Dado que este proyecto se limitó al rendimiento numérico, se recomienda que futuras iteraciones incorporen variables socioeconómicas y sociodemográficas (ausentismo, distancia al colegio o nivel de instrucción de tutores). La literatura sugiere que estos predictores reducen significativamente el volumen de Falsos Positivos, afinando la precisión general de los algoritmos.
