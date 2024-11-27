import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Catalog = () => {
  const [parts, setParts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [filters, setFilters] = useState({
    category: '',
    manufacturer: '',
    search: ''
  });

  useEffect(() => {
    const fetchParts = async () => {
      try {
        const res = await axios.get('/api/parts', { params: filters });
        setParts(res.data);
        setLoading(false);
      } catch (err) {
        setError('Ошибка загрузки каталога');
        setLoading(false);
      }
    };

    fetchParts();
  }, [filters]);

  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value
    });
  };

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div className="alert alert-danger">{error}</div>;

  return (
    <div className="catalog">
      <h2>Каталог автозапчастей</h2>
      
      <div className="filters">
        <input
          type="text"
          name="search"
          placeholder="Поиск..."
          value={filters.search}
          onChange={handleFilterChange}
          className="form-control"
        />
        
        <select
          name="category"
          value={filters.category}
          onChange={handleFilterChange}
          className="form-control"
        >
          <option value="">Все категории</option>
          <option value="Engine">Двигатель</option>
          <option value="Transmission">Трансмиссия</option>
          <option value="Brake System">Тормозная система</option>
          <option value="Suspension">Подвеска</option>
          <option value="Electrical">Электрика</option>
          <option value="Body Parts">Кузовные детали</option>
          <option value="Interior">Салон</option>
        </select>
        
        <select
          name="manufacturer"
          value={filters.manufacturer}
          onChange={handleFilterChange}
          className="form-control"
        >
          <option value="">Все производители</option>
          <option value="Toyota">Toyota</option>
          <option value="Honda">Honda</option>
          <option value="Ford">Ford</option>
          <option value="BMW">BMW</option>
          <option value="Mercedes">Mercedes</option>
        </select>
      </div>

      <div className="parts-grid">
        {parts.map(part => (
          <div key={part._id} className="part-card">
            <img src={part.images[0]} alt={part.name} className="part-image" />
            <div className="part-info">
              <h3>{part.name}</h3>
              <p>{part.manufacturer}</p>
              <p className="price">{part.price} руб.</p>
              <div className="part-actions">
                <Link to={`/parts/${part._id}`} className="btn btn-primary">
                  Подробнее
                </Link>
                <button className="btn btn-secondary">В корзину</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Catalog;
