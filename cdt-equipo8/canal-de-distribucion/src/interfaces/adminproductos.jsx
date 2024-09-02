import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/adminproductos.css';

const AdminProductos = () => {
  const [products, setProducts] = useState([]);
  const [hoveredProduct, setHoveredProduct] = useState(null);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const [productsResponse, detailsResponse, photosResponse] = await Promise.all([
          axios.get('http://127.0.0.1:8000/api/agr-productos/?format=json'),
          axios.get('http://127.0.0.1:8000/api/agr-detalleproductos/?format=json'),
          axios.get('http://127.0.0.1:8000/api/agr-fotos/?format=json')
        ]);

        const productsData = productsResponse.data;
        const detailsData = detailsResponse.data;
        const photosData = photosResponse.data;

        const combinedData = productsData.map(product => {
          const detail = detailsData.find(detail => detail.producto === product.idproducto);
          const photos = photosData.filter(photo => photo.producto === product.idproducto);
          return {
            ...product,
            detail,
            photos
          };
        });

        setProducts(combinedData);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  const handleSort = (key) => {
    let direction = 'asc';
    if (sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });
  };
  
  const sortedProducts = React.useMemo(() => {
    let sortableProducts = [...products];
    if (sortConfig.key !== null) {
      sortableProducts.sort((a, b) => {
        let aValue = a;
        let bValue = b;
  
        const keys = sortConfig.key.split('.');
        keys.forEach(key => {
          aValue = aValue ? aValue[key] : undefined;
          bValue = bValue ? bValue[key] : undefined;
        });
  
        // Convert tamaño to a number if it's a string with numbers and optional " character
        if (sortConfig.key === 'detail.tamaño') {
          aValue = parseFloat(aValue.replace(/[^0-9.]/g, ''));
          bValue = parseFloat(bValue.replace(/[^0-9.]/g, ''));
        } else {
          if (typeof aValue === 'string' && typeof bValue === 'string') {
            aValue = aValue.toUpperCase();
            bValue = bValue.toUpperCase();
          }
        }
  
        if (aValue < bValue) {
          return sortConfig.direction === 'asc' ? -1 : 1;
        }
        if (aValue > bValue) {
          return sortConfig.direction === 'asc' ? 1 : -1;
        }
        return 0;
      });
    }
    return sortableProducts;
  }, [products, sortConfig]);

  return (
    <div className="inventory-container">
      <div className="photo-preview">
        {hoveredProduct && hoveredProduct.photos.length > 0 && (
          <img src={hoveredProduct.photos[0].link} alt={hoveredProduct.nombre} />
        )}
      </div>
      <table className="product-table">
        <thead>
          <tr>
            <th
              onClick={() => handleSort('nombre')}
              className={sortConfig.key === 'nombre' ? 'sortable active' : 'sortable'}
            >
              Nombre
            </th>
            <th
              onClick={() => handleSort('stock')}
              className={sortConfig.key === 'stock' ? 'sortable active' : 'sortable'}
            >
              Cantidad
            </th>
            <th
              onClick={() => handleSort('detail.precio')}
              className={sortConfig.key === 'detail.precio' ? 'sortable active' : 'sortable'}
            >
              Precio
            </th>
            <th
              onClick={() => handleSort('detail.tamaño')}
              className={sortConfig.key === 'detail.tamaño' ? 'sortable active' : 'sortable'}
            >
              Tamaño
            </th>
            <th
              onClick={() => handleSort('detail.marca')}
              className={sortConfig.key === 'detail.marca' ? 'sortable active' : 'sortable'}
            >
              Marca
            </th>
          </tr>
        </thead>
        <tbody>
          {sortedProducts.map(product => (
            <tr
              key={product.idproducto}
              onMouseEnter={() => setHoveredProduct(product)}
              onMouseLeave={() => setHoveredProduct(product)}
            >
              <td>{product.nombre}</td>
              <td className={product.stock > 0 ? 'in-stock' : 'out-of-stock'}>{product.stock}</td>
              <td>{product.detail ? product.detail.precio : 'N/A'}</td>
              <td>{product.detail ? product.detail.tamaño : 'N/A'}</td>
              <td>{product.detail ? product.detail.marca : 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminProductos;
