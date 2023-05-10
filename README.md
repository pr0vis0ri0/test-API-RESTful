# test-API-RESTful

Este repositorio está creado con el fin de probar cómo funcionaría la conexión entre dos proyectos django siendo uno el responsable del frontend y otro del backend, conectándose por medio de una API RESTful.

Edit 09-05-2023 : Logré que el backend sea una API REST por sí sola y se puede conseguir información como registrar, ahora sólo queda enviar dicha información al frontend.

Edit 09-05-2023 17:16 - Se logró, hice que el backend se conectara con el frontend a través de una petición Ajax y retorne la información en un tipo JSON para después colocarla en un div.

Edit 10-05-2023 : Hice un mayor avance al hacer que el frontend hiciste petición de datos del backend por medio de las views.py importando las requests y retornando data en formato JSON para luego mostrarla en bloques de Django con loops for.
