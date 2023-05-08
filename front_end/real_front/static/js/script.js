import axios from 'axios'

axios.get('http://localhost:8000/back/api/departamentos/')
.then(function (response) {
    const departamentos = response.data;
    const listaDepartamentos = document.querySelector('#departamentos');
    departamentos.forEach(function(departamento) {
        const li = document.createElement('li');
        li.textContent = `${departamento.tipo_departamento} - ${departamento.precio_departamento} - ${departamento.direccion_departamentos} - ${departamento.metros_departamento}`;
        listaDepartamentos.appendChild(li);
    });
})
.catch(function (error) {
    console.log(error);
});