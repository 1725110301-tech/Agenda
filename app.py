import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/contactos', 'controllers.lista_contactos.ListaContactos',
    '/contacto/(\\d+)', 'controllers.ver_contacto.VerContacto',
    '/nuevo', 'controllers.insertar_contacto.NuevoContacto',
    '/editar/(\\d+)', 'controllers.modificar_contacto.EditarContacto',
    '/borrar/(\\d+)', 'controllers.borrar_contacto.BorrarContacto',
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()