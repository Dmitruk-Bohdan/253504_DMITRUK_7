import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import axios from 'axios';

const PartDetails = () => {
  const { id } = useParams();
  const { isAuthenticated } = useAuth();
  const [part, setPart] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [quantity, setQuantity] = useState(1);

  useEffect(() => {
    const fetchPart = async () => {
      try {
        const res = await axios.get(`/api/parts/${id}`);
        setPart(res.data);
        setLoading(false);
      } catch (err) {
        setError('Ошибка загрузки информации о товаре');
        setLoading(false);
      }
    };

    fetchPart();
  }, [id]);

  const handleAddToCart = async () => {
    if (!isAuthenticated) {
      // Перенаправление на страницу входа
      window.location.href = '/login';
      return;
    }

    try {
      await axios.post('/api/cart', {
        partId: id,
        quantity
      });
      alert('Товар добавлен в корзину');
    } catch (err) {
      alert('Ошибка при добавлении в корзину');
    }
  };

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div className="alert alert-danger">{error}</div>;
  if (!part) return <div>Товар не найден</div>;

  return (
    <div className="part-details">
      <div className="part-images">
        <img src={part.images[0]} alt={part.name} className="main-image" />
        <div className="image-gallery">
          {part.images.slice(1).map((image, index) => (
            <img key={index} src={image} alt={`${part.name} ${index + 2}`} />
          ))}
        </div>
      </div>

      <div className="part-info">
        <h1>{part.name}</h1>
        <div className="part-meta">
          <p>Производитель: {part.manufacturer}</p>
          <p>Категория: {part.category}</p>
          <p>Модель: {part.model}</p>
          <p>Год: {part.year}</p>
        </div>

        <div className="part-price">
          <h2>{part.price} руб.</h2>
          <p className="stock-status">
            {part.stock > 0 ? 'В наличии' : 'Нет в наличии'}
          </p>
        </div>

        {part.stock > 0 && (
          <div className="purchase-controls">
            <div className="quantity-control">
              <button
                onClick={() => setQuantity(Math.max(1, quantity - 1))}
                className="btn btn-secondary"
              >
                -
              </button>
              <input
                type="number"
                min="1"
                max={part.stock}
                value={quantity}
                onChange={(e) => setQuantity(Number(e.target.value))}
                className="form-control"
              />
              <button
                onClick={() => setQuantity(Math.min(part.stock, quantity + 1))}
                className="btn btn-secondary"
              >
                +
              </button>
            </div>
            <button
              onClick={handleAddToCart}
              className="btn btn-primary add-to-cart"
            >
              Добавить в корзину
            </button>
          </div>
        )}

        <div className="part-description">
          <h3>Описание</h3>
          <p>{part.description}</p>
        </div>

        <div className="part-specifications">
          <h3>Характеристики</h3>
          <div className="specs-grid">
            {Object.entries(part.specifications || {}).map(([key, value]) => (
              <div key={key} className="spec-item">
                <span className="spec-key">{key}:</span>
                <span className="spec-value">{value}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default PartDetails;
