document.addEventListener('DOMContentLoaded', function() {
    const InputBusqueda = document.getElementById('search-input');
    const botonesVet = document.querySelectorAll('.vet-locations');

    InputBusqueda.addEventListener('input', function() {
        filtroVetLocalidad();

    })

    function filtroVetLocalidad() {
        const texto = InputBusqueda.value.tolowerCase();
        botonesVet.forEach(boton => {
            const localidad = boton.getAttribute('data-localidad').tolowerCase();
            if (localidad.include(texto)) {
                boton.style.display = '';
            } else {
                boton.style.display = 'none';
            }


        });

    }

});