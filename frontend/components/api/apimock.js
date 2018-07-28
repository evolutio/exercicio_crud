import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
    add_todo(newtask){
        return mockasync({description: newtask, done: false});
    },
    list_todos(){
        return mockasync({
            todos: [
                {description: 'Do the laundry', done: true},
                {description: 'Walk the dog', done: false}
            ]
        });
    },
    list_pais(){
        return mockasync(pais)
    },
    save_pai(pai){
        if (!pai.id) {
            pai.id = ++ID
            pais.push(pai)
        }
        return mockasync(pai)
    },
    get_pai(id) {
        return mockasync(pais.filter(pai => pai.id == id)[0])
    },
    remove_pai(id) {
        return mockasync({})
    }
};

let pais = [
    {id: 1, name: 'Tony Lampada', countfilhos: 2, maisvelho: '7 anos'},
    {id: 2, name: 'Régis Feelings', countfilhos: 2, maisvelho: 'Espoleta'},
    {id: 3, name: 'Elias Cabeçudo', countfilhos: 8, maisvelho: 'cabecinha'},
]

let ID = 5000

export default api;
