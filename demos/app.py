import web

urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    '/contacto/(\\d+)', 'VerContacto',
    '/nuevo', 'NuevoContacto',
    '/editar/(\\d+)', 'EditarContacto',
    '/borrar/(\\d+)', 'BorrarContacto',
)

app = web.application(urls, globals())
render = web.template.render('views')

# Datos en memoria (temporal, después los conectamos a BD con el profe)
contactos = [
    {'id': 1, 'nombre': 'Juan Pérez',    'telefono': '771-123-4567', 'email': 'juan@correo.com',  'direccion': 'Calle 1, Pachuca'},
    {'id': 2, 'nombre': 'María López',   'telefono': '771-987-6543', 'email': 'maria@correo.com', 'direccion': 'Av. 2, Tulancingo'},
    {'id': 3, 'nombre': 'Carlos Soto',   'telefono': '771-555-0000', 'email': 'carlos@correo.com','direccion': 'Col. Centro, Hidalgo'},
]
next_id = 4


class Index:
    def GET(self):
        return render.index()


class Contactos:
    def GET(self):
        return render.contactos(contactos)


class VerContacto:
    def GET(self, id):
        contacto = next((c for c in contactos if c['id'] == int(id)), None)
        if not contacto:
            raise web.notfound()
        return render.ver_contacto(contacto)


class NuevoContacto:
    def GET(self):
        return render.nuevo()

    def POST(self):
        global next_id
        datos = web.input()
        contactos.append({
            'id': next_id,
            'nombre':    datos.nombre,
            'telefono':  datos.telefono,
            'email':     datos.email,
            'direccion': datos.direccion,
        })
        next_id += 1
        raise web.seeother('/contactos')


class EditarContacto:
    def GET(self, id):
        contacto = next((c for c in contactos if c['id'] == int(id)), None)
        if not contacto:
            raise web.notfound()
        return render.editar(contacto)

    def POST(self, id):
        datos = web.input()
        for c in contactos:
            if c['id'] == int(id):
                c['nombre']    = datos.nombre
                c['telefono']  = datos.telefono
                c['email']     = datos.email
                c['direccion'] = datos.direccion
                break
        raise web.seeother('/contactos')


class BorrarContacto:
    def POST(self, id):
        global contactos
        contactos = [c for c in contactos if c['id'] != int(id)]
        raise web.seeother('/contactos')


if __name__ == '__main__':
    app.run()
