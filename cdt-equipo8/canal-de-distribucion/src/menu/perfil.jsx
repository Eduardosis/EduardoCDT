import React from 'react';

const Perfil = () => {
  // un ejemplito para ver como se ve el perfil
  const proveedor = {
    nombre: 'Josee',
    apellidoPaterno: 'Ramirezz',
    apellidoMaterno: 'Aispurooo',
    telefono: '6642333677',
    empresa: 'Apple'
  };

  return (
    <div>
      <h1>Perfil de Proveedor</h1>
      <div>
        <p><strong>Nombre:</strong> {proveedor.nombre}</p>
        <p><strong>Apellido Paterno:</strong> {proveedor.apellidoPaterno}</p>
        <p><strong>Apellido Materno:</strong> {proveedor.apellidoMaterno}</p>
        <p><strong>Telefono:</strong> {proveedor.telefono}</p>
        <p><strong>Empresa:</strong> {proveedor.empresa}</p>
      </div>
      <div>
        <p><strong>Rol:</strong> Proveedor</p>
      </div>
    </div>
  );
};

export default Perfil;