import web

render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    

if __name__ == '__main__':
    app.run()