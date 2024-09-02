import React, { useEffect, useState } from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './styles/styles.css';
import logo from './img/logo.png';

import Perfil from './menu/perfil.jsx';
import InfoAlmacen from './menu/infoalmacen.jsx';
import Configuracion from './menu/configuracion.jsx';
import Productos from './interfaces/productos.jsx';
import ReporteProductos from './interfaces/reporteprod.jsx';
import ReporteEnvios from './interfaces/reporteenv.jsx';
import ReporteEntrega from './interfaces/reporteent.jsx';
import OrdenEnvio from './interfaces/ordenenvio.jsx';
import Admin from './interfaces/admin.jsx';
import AdminProductos from './interfaces/adminproductos.jsx';
import Genreporteprod from './interfaces/genreporteprod.jsx';
//import Admin from './interfaces/admin.jsx';


const Home = ({ handleNavigate }) => {
  return (
    <div className="content-panel">
      <h1>Panel de Proveedores</h1>
      <div className="button-container-panel">
      <button onClick={() => handleNavigate('/reporteprod')}>Reportes de Productos</button>
        <button onClick={() => handleNavigate('/reporteenv')}>Reportes de Envios</button>
        <button onClick={() => handleNavigate('/reporteent')}>Reportes de Entrega</button>
        <button onClick={() => handleNavigate('/ordenenvio')}>Orden de Envio</button>
        <button onClick={() => handleNavigate('/productos')}>Productos</button>      </div>
    </div>
  );
};

const App = () => {
  const [productos, setProductos] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [menuOpen, setMenuOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/productos/')
      .then(response => {
        setProductos(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the productos!', error);
      });

    axios.get('http://127.0.0.1:8000/api/categorias/')
      .then(response => {
        setCategorias(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the categorias!', error);
      });
  }, []);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  const handleNavigate = (path) => {
    navigate(path);
  };

  return (
    <div>
      <header>
        <div className="container">
          <div>
          <img className='logo' src={logo} alt="Logo" onClick={() => handleNavigate('/')} />
          </div>
          <div className="header-title">CANAL DE DISTRIBUCIÓN TECNOLÓGICO</div>
          <div className="menu-icon" onClick={toggleMenu}>☰</div>
        </div>
      </header>
      <div className={`menu ${menuOpen ? 'open' : ''}`}>
        <ul>
          <li className= 'menuoption' onClick={() => handleNavigate('/')}>Home</li>
          <li className= 'menuoption' onClick={() => handleNavigate('/perfil')}>Perfil</li>
          <li className= 'menuoption' onClick={() => handleNavigate('/infoalmacen')}>Informacion de almacen</li>
          <li className= 'menuoption' onClick={() => handleNavigate('/admin')}>Administrador</li>

          <li className='cierre'>Cerrar sesión</li>
        </ul>
      </div>
      <main className={`main ${menuOpen ? 'menu-open' : ''}`}>
        <Routes>
        <Route path="/" element={<Home handleNavigate={handleNavigate} />} />
          <Route path="/productos" element={<Productos />} />
          <Route path="/perfil" element={<Perfil />} />
          <Route path="/infoalmacen" element={<InfoAlmacen />} />
          <Route path="/configuracion" element={<Configuracion />} />
          <Route path="/reporteprod" element={<ReporteProductos />} />
          <Route path="/reporteenv" element={<ReporteEnvios />} />
          <Route path="/reporteent" element={<ReporteEntrega />} />
          <Route path="/ordenenvio" element={<OrdenEnvio />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/admin/adminproductos" element={<AdminProductos />} />
          <Route path="/admin/genreporteprod" element={<Genreporteprod />} />

        </Routes>
      </main>
      <div className={`overlay ${menuOpen ? 'open' : ''}`} onClick={toggleMenu}></div>
      <footer>
        <div className="container">
        Si tienes dudas contactar a: 
          <a href="https://wa.me/526647958688" target="_blank" rel="noopener noreferrer">
            664 795 86 88
          </a>        
        </div>
      </footer>
    </div>
  );
};

export default App;