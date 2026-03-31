====================================================================================
  Evi Portable — Manual de usuario (descripción general)
  Documento: Inglés • Se aplica a la compilación que recibió con esta carpeta
====================================================================================

Coloque aquí también sus propias guías o traducciones más extensas (por ejemplo, EN_User_Manual.pdf,
DE_Handbuch.txt). Este archivo es opcional para que Evi lo ejecute; es para que lo leas
o imprimir.

Copias localizadas: README_<LANG>.txt y FEHLERSUCHE_<LANG>.txt en esta carpeta
(los mismos códigos de idioma que la interfaz de usuario del sitio web). Descripción general en inglés: este README.txt;
Solución de problemas en inglés: FEHLERSUCHE_EN.txt. La solución de problemas en alemán también es
mantenido a mano como FEHLERSUCHE_DE.txt.

Índice de carpeta (nombramiento de archivos, generador): README.md

--------------------------------------------------------------------------------
  Sistema operativo
--------------------------------------------------------------------------------

Evi Portable es solo para Microsoft Windows 10 y Windows 11. no lo es
compatible con Windows 7/8, macOS, Linux o sistemas operativos móviles.

--------------------------------------------------------------------------------
  Primer inicio: desde la descarga hasta la ejecución de Evi
--------------------------------------------------------------------------------

1) Ubicación de instalación
   Copie o extraiga toda la carpeta Evi a un lugar que usted controle, por ejemplo
   su escritorio, documentos o una memoria USB. Mantenga la estructura de carpetas como
   entregado (no elimine subcarpetas que no haya creado usted mismo).

2) Modelo de lenguaje (obligatorio)
   Evi necesita un archivo de modelo de IA principal (extensión .gguf) en la carpeta:
   modelos\llm\
   Consulte models\llm\README.txt para obtener recomendaciones de tamaño. Una vez que el archivo esté allí,
   iniciar Evi; detecta el modelo automáticamente cuando es posible.

3) Primer lanzamiento: activación
   Cuando inicias Evi por primera vez, aparece una ventana de activación.
   • Su PC muestra una ID de máquina (exclusiva de este hardware).
   • Copie el ID de la Máquina (botón: "Copiar ID de la Máquina") y envíelo por correo electrónico a:
     Brielbeck@hotmail.de
   • Recibirás una clave de serie que funciona solo en esa misma PC
     (la clave está vinculada a su hardware).
   • Pegue la clave en la ventana de activación y elija Activar.

   Si cambia hardware importante o mueve el disco de una manera que cambie la ID,
   es posible que necesite una nueva clave; comuníquese con la misma dirección.

4) Después de la activación
   Se abre la ventana principal. Elija idioma, micrófono y voz en la izquierda
   panel de configuración. Di "abre la hoja de trucos" en cualquier momento para ver ejemplos de comandos
   (consulte las hojas de trucos\en.txt y los archivos hermanos para otros idiomas).

5) Opcional: abre este manual desde Windows
   En el Explorador de archivos, vaya a la carpeta Evi, luego Manual\README.txt y ábralo.
   con el Bloc de notas o cualquier visor de texto.

--------------------------------------------------------------------------------
  Idioma de la interfaz (GUI)
--------------------------------------------------------------------------------

La interfaz de usuario sigue el idioma que elija en Idioma en la parte superior
del panel de configuración izquierdo (primer bloque en la barra lateral). Después de seleccionar un
El idioma, los menús, los botones, las etiquetas y la mayor parte del texto en pantalla cambian a ese
idioma dondequiera que existan traducciones. Puedes cambiarlo en cualquier momento; solo el
La redacción cambia, no el diseño.

Consejo: Las hojas de trucos de comandos en la carpeta Cheatsheets\ se enumeran por
código de idioma (en.txt, de.txt,…). Para obtener más información, consulte hojas de trucos\README.txt.
Esta carpeta Manual\ es la descripción general más extensa del producto; las hojas de trucos son las
lista rápida de "qué decir".

--------------------------------------------------------------------------------
  Tarjeta gráfica (GPU): guía rápida
--------------------------------------------------------------------------------

Una buena opción intermedia es una NVIDIA GeForce RTX 4070 Ti con 12 GB de vídeo
Memoria: buen equilibrio entre velocidad, tamaño del contexto y espacio para modelos más grandes.

Las tarjetas desde aproximadamente RTX 3060 hasta RTX 5090 pueden funcionar bien; el mejor ajuste depende
sobre RAM, CPU, refrigeración y qué archivo de modelo instala. Utilice el ajuste preestablecido de GPU en
La barra lateral de Evi se adapta a tu hardware.

La ejecución solo en la CPU (los ajustes preestablecidos "CPU... GB RAM") es una alternativa de emergencia:
Evi sigue siendo utilizable sin una tarjeta gráfica adecuada, pero las respuestas son mucho más lentas.
Prefiere una GPU real siempre que puedas.

--------------------------------------------------------------------------------
  Totalmente portátil: cuando necesitas Internet
--------------------------------------------------------------------------------

Evi está diseñado para ser portátil: copie la carpeta completa a otra unidad, memoria USB,
o PC, luego inícielo allí. Chats, recuerdos, configuraciones, datos de seguridad y su
El archivo de activación normalmente permanece dentro de esa carpeta (la activación está ligada al
PC, no la ruta de la carpeta).

Internet es principalmente para cosas que usted elige descargar (archivos de modelo, opcionales).
voces o extras, actualizaciones) y para funciones opcionales como búsqueda web, correo,
streaming o el clima cuando permites el acceso a la red.

Chat principal, memoria, notas, temporizadores, herramientas de archivos dentro de su carpeta permitida, local
reconocimiento de voz, salida de voz local y bloqueo de privacidad ejecutados en su
máquina sin enviar sus conversaciones a un servicio en la nube. Opcional en línea
Las funciones solo se ejecutan cuando el acceso a la red está activado y usted las usa.

--------------------------------------------------------------------------------
  Seguridad: PIN y desbloqueo por voz (anticopia)
--------------------------------------------------------------------------------

Evi puede utilizar un PIN de seguridad y un registro de voz opcional en su dispositivo.

Cuando se utiliza el desbloqueo por voz, cada intento puede solicitar un breve conjunto de palabras aleatorias
eso cambia cada vez, no una frase fija para siempre. Eso bloquea lo fácil
truco de reproducir una única grabación antigua de tu voz. Su PIN sigue siendo un
línea de defensa separada.

Esto está diseñado para detener el abuso casual; ningún producto de consumo puede prometer
perfección contra cada ataque (por ejemplo, alguien que tiene tanto su PIN como su
mímica de voz sofisticada). Mantenga su PIN privado y complete la configuración como
La aplicación te guía.

--------------------------------------------------------------------------------
  Solución de problemas (lista de verificación breve)
--------------------------------------------------------------------------------

• No hay respuestas de IA/error de modelo
  → ¿Al menos un .gguf adecuado en models\llm\? Consulte modelos\llm\README.txt.
  → Pruebe con un modelo más pequeño o una CPU preestablecida en la barra lateral si falla la ruta de la GPU.

• Sin micrófono
  → Configuración de sonido de Windows: prueba el micrófono. En Evi, elige el dispositivo debajo
    Micrófono y Guardar.

• Sin salida de voz
  → Verifique que existan archivos de voz para su idioma en la carpeta piper\ y
    Elige una voz en la barra lateral.

• Web o YouTube fallan
  → Desactive "Bloquear todo el tráfico" en la barra lateral si desea funciones en línea.
  → Para la reproducción de YouTube, normalmente se requiere VLC Portable y acceso a la red.

• Después de editar las hojas de trucos
  → Reinicie Evi para que todos los asistentes de texto detecten los cambios de manera confiable.

--------------------------------------------------------------------------------
  Solución de problemas (referencia ampliada)
--------------------------------------------------------------------------------

Comprobaciones rápidas (siempre primero)
  • ¿Windows 10 u 11 de 64 bits, actualizado y reiniciado después de grandes cambios?
  • ¿Evi se ejecuta desde una carpeta completamente extraída, no desde dentro de un archivo?
  • Evite las carpetas sincronizadas en la nube (OneDrive, etc.) para la carpeta de datos en vivo mientras
    Evi se ejecuta: utilice una ruta local como C:\EviPortable o D:\Tools\Evi cuando
    posible.
  • ¿Suficiente espacio libre en disco para el modelo, los chats y las actualizaciones?
  • Después de cambiar modelos, voces u hojas de trucos: salga de Evi por completo y comience
    otra vez.

1) sistema operativo
  • Evi es solo para Windows 10 y 11; otras versiones del sistema operativo no son compatibles.
  • Si la aplicación no se inicia en absoluto, extraiga completamente el paquete, verifique el antivirus
    registros de ejecutables bloqueados y pruebe una ruta de instalación más corta sin raras
    Caracteres solo Unicode.

2) Ruta de la carpeta, antivirus, portabilidad.
  • Agregue una exclusión para su carpeta raíz de Evi en el software de seguridad si los escaneos fallan.
    el inicio es muy lento o bloquea archivos durante las descargas.
  • Memorias USB: prefiera USB 3 + NTFS; Los medios muy lentos hacen que los modelos grandes sean dolorosos.

3) Modelo de lenguaje (.gguf)
  • Síntomas: falta de respuestas, errores de modelo, fallo instantáneo al cargar.
  • correcciones: verificar que models\llm\ contenga un .gguf completo (no 0 bytes); volver a descargar
si es necesario; haga coincidir el tamaño del modelo con la VRAM usando models\llm\README.txt; si no está seguro,
    mantenga un único archivo q4_k_m probado en la carpeta.
  • múltiples archivos .gguf: Evi puede elegir el más grande que se ajuste a su VRAM, si
    Si sospecha un conflicto, pruebe con un solo archivo.

4) GPU, CUDA, controladores, falta de memoria
  • Actualizar el controlador NVIDIA; en portátiles, fuerce la GPU/rendimiento discreto
    modo para Evi donde Windows lo permite.
  • Si ve fallas de OOM o GPU, use un punto de control más pequeño, cierre otras aplicaciones de GPU,
    baje la temperatura o cambie a un valor preestablecido de la CPU (más lento pero más estable).

5) modo solo CPU
  • Se espera que sea lento; liberar suficiente RAM del sistema; cerrar tareas pesadas en segundo plano;
    utilizar plan de energía "Alto rendimiento" durante sesiones largas.

6) Activación
  • Pegue las claves con cuidado (sin espacios adicionales); Las claves están vinculadas a una ID de máquina.
  • Después de cambios importantes de hardware, es posible que necesite una clave de reemplazo; utilice el servicio de soporte
    dirección con tus datos.

7) micrófono
  • Privacidad de Windows → Micrófono → permitir aplicaciones de escritorio.
  • Configure el dispositivo de grabación predeterminado correcto; en Evi elige el mismo dispositivo y Guardar.
  • Los auriculares Bluetooth pueden agregar latencia; pruebe con un micrófono USB si no está seguro.
  • Otra aplicación puede mantener el modo exclusivo: cerrar el software de reuniones temporalmente.

8) Reconocimiento de voz (local)
  • Si el reconocimiento nunca finaliza, asegúrese de que los archivos de modelo en models\whisper estén
    intacto y permitir la red en la primera recuperación del modelo si su compilación lo necesita.

9) Salida de voz (Piper / TTS)
  • Confirma que piper\ contiene un paquete de voz para tu idioma de interfaz de usuario; elige una voz en
    la barra lateral; verifique el mezclador de volumen de Windows: es posible que Evi esté silenciado por aplicación.

10) Red y "Bloquear todo el tráfico"
  • Desactive el bloqueo de web, ayudas de correo, clima o descargas.
  • Los servidores proxy corporativos o las VPN pueden requerir ayuda de TI para las listas de permitidos.

11) YouTube y los medios
  • Conservar el diseño VLC Portable incluido; habilitar el acceso a la red; leer
    Portable\VLCPortable guía si la ruta fue movida.

12) Idioma de la interfaz de usuario y hojas de referencia
  • Las hojas de referencia están por archivo de idioma en hojas de referencia\; consulte hojas de referencia\README.txt.
  • Guardar las ediciones como UTF-8; reinicie Evi después de las ediciones.

13) Seguridad (PIN / desbloqueo por voz)
  • Utilice un ambiente tranquilo; vuelva a comprobar la ganancia del micrófono; nunca compartas tu PIN.
  • Las indicaciones de palabras aleatorias son intencionales: las grabaciones de voz antiguas no deberían desbloquearse.

14) Rendimiento, congelaciones, fallas
  • Reduzca el tamaño del modelo, mejore la refrigeración, lea cualquier crash.log en el árbol si su
    build crea uno y revierte el último cambio que realizó antes de las fallas.

15) Al contactar al soporte
  • Incluya ID de máquina, versión de Windows, modelo de GPU + VRAM + controlador, cuyo formato .gguf
    que utiliza y el texto de error exacto (no las claves secretas).

Referencia completa de solución de problemas (este idioma): Manual\FEHLERSUCHE_ES.txt

--------------------------------------------------------------------------------
  Soporte: claves de serie e ID de máquina
--------------------------------------------------------------------------------

Correo electrónico: Brielbeck@hotmail.de
Incluya siempre su ID de máquina en la pantalla de activación cuando solicite una
clave de serie o una clave de reemplazo después de cambios de hardware.

====================================================================================