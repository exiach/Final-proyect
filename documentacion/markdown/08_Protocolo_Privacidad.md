# Protocolo de privacidad y uso responsable

## Alcance

El proyecto procesa calificaciones y datos administrativos de estudiantes de
educación primaria. Por tratarse de menores, la información debe manejarse con
acceso restringido y únicamente para fines pedagógicos autorizados.

## Controles mínimos

1. Obtener autorización escrita de la dirección de la unidad educativa.
2. Sustituir el RUDE por un identificador seudónimo antes del modelado.
3. Excluir nombres, apellidos, número de identidad y lugar de nacimiento del
   dataset utilizado para entrenamiento y evaluación.
4. Mantener los archivos originales fuera de repositorios públicos.
5. Restringir el acceso al prototipo a personal autorizado.
6. No utilizar una alerta como decisión automática, sanción o diagnóstico.
7. Registrar la revisión humana y la intervención adoptada.
8. Eliminar cargas temporales después de la sesión y definir un plazo de
   conservación para los datos históricos.

## Implementación disponible

- `data/` permanece excluido de Git; `data_demo/` contiene únicamente registros
  ficticios para demostración pública.
- El prototipo no incorpora autenticación ni modos seleccionables mediante variables
  de entorno. Debe ejecutarse únicamente en un equipo local controlado y no debe
  publicarse ni desplegarse en un entorno accesible a terceros.
- La interfaz muestra un código SHA-256 abreviado en lugar del RUDE.
- Las salidas conservadas en los notebooks de modelado son agregadas; los
  cuadernos que procesan datos individuales mantienen sus salidas eliminadas.

Estos controles reducen exposición accidental, pero no sustituyen la autorización
institucional, la gestión de roles, el cifrado ni una política formal de retención
en un despliegue productivo.

## Limitación de uso

El sistema es un prototipo exploratorio. Una alerta señala necesidad de revisión
docente; no demuestra por sí sola una dificultad de aprendizaje ni reemplaza la
evaluación pedagógica integral.
