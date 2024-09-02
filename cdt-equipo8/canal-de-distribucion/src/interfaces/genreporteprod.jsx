import React, { useState } from 'react';
import '../styles/genreporteprod.css'; 

const Genreporteprod = () => {
  const [selectedBrand, setSelectedBrand] = useState('');
  const [selectedModel, setSelectedModel] = useState('');
  const [quantity, setQuantity] = useState('');
  const [price, setPrice] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');

  const hpModels = ['a1234', 'a5678', 'a9012'];
  const dellModels = ['b1234', 'b5678', 'b9012'];

  const handleBrandChange = (e) => {
    setSelectedBrand(e.target.value);
    setSelectedModel('');
  };

  const getModelOptions = () => {
    if (selectedBrand === 'Laptop HP') {
      return hpModels;
    } else if (selectedBrand === 'Laptop Dell') {
      return dellModels;
    } else {
      return [];
    }
  };

  return (
    <div className="admin-container">
      <div className="form-group">
        <select
          className="admin-button"
          value={selectedBrand}
          onChange={handleBrandChange}
        >
          <option value="">Seleccione una marca</option>
          <option value="Laptop HP">Laptop HP</option>
          <option value="Laptop Dell">Laptop Dell</option>
        </select>

        <select
          className="admin-button"
          value={selectedModel}
          onChange={(e) => setSelectedModel(e.target.value)}
          disabled={!selectedBrand}
        >
          <option value="">Seleccione un modelo</option>
          {getModelOptions().map((model) => (
            <option key={model} value={model}>
              {model}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <input
          type="number"
          className="admin-button"
          placeholder="Cantidad"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />
        <input
          type="number"
          className="admin-button"
          placeholder="Precio"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
        <select
          className="admin-button"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        >
          <option value="">Seleccione una categoría</option>
          <option value="Laptop">Laptop</option>
          <option value="Teléfono">Teléfono</option>
        </select>
      </div>

      <div className="form-group">
        <textarea
          className="admin-button"
          placeholder="Descripción"
          rows="4"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        ></textarea>
      </div>
    </div>
  );
};

export default Genreporteprod;