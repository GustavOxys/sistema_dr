var btnlogin = document.querySelector('#login');
var btnregister = document.querySelector('#register');
var body = document.querySelector('body');

btnlogin.addEventListener('click', function () {
    body.className = 'login-js';
});

btnregister.addEventListener('click', function () {
    body.className = 'register-js';
})