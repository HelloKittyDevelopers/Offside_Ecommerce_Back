import React from 'react'
/*
En HTML, la etiqueta span es un elemento contenedor en línea genérico. 
Las etiquetas span generalmente envuelven secciones de texto con fines de estilo o 
para agregar atributos a una sección de texto sin crear una nueva línea de contenido.
*/
function Rating({ value, text, color = '#f8e825' }) {
    return (
        <div className="rating">
            {[1, 2, 3, 4, 5].map((star) => (
                <span key={star}>
                    <i
                        style={{ color }}
                        className={
                            value >= star
                                ? 'fas fa-star'
                                : value >= star - 0.5
                                ? 'fas fa-star-half-alt'
                                : 'far fa-star'
                        }
                    ></i>
                </span>
            ))}
            {text && <span>{text}</span>}
        </div>
    );
}

export default Rating;