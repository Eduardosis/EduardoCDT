import React from 'react';
import "../styles/admin.css";
import { useNavigate } from 'react-router-dom';

function Admin() {
    const navigate = useNavigate();

    const handleButtonClick = () => {
        navigate('AdminProductos'); 
    };

    const handleReporteProductoClick = () => {
        navigate('genreporteprod');
    };

    return (
        <div>
            <h1>Administrador</h1>
            <div className="admin-container">
                <button className="admin-button">Reporte Envío</button>
                <button className="admin-button">Reporte Entrega</button>
                <button className="admin-button" onClick={handleReporteProductoClick}>Reporte Producto</button>
                <button className="admin-button" onClick={handleButtonClick}>Productos</button>
            </div>
        </div>
    );
}

export default Admin;