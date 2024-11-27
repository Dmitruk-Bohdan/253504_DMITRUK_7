import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [total, setTotal] = useState(0);

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    try {
      const res = await axios.get('/api/cart');
      setCartItems(res.data);
      calculateTotal(res.data);
      setLoading(false);
    } catch (err) {
      setError('Ошибка загрузки корзины');
      setLoading(false);
    }
  };

  const calculateTotal = (items) => {
    const sum = items.reduce((acc, item) => {
      return acc + (item.part.price * item.quantity);
    }, 0);
    setTotal(sum);
  };

  const updateQuantity = async (itemId, newQuantity) => {
    if (newQuantity < 1) return;
    
    try {
      await axios.put(`/api/cart/${itemId}`, {
        quantity: newQuantity
      });
      
      const updatedItems = cartItems.map(item => {
        if (item._id === itemId) {
          return { ...item, quantity: newQuantity };
        }
        return item;
      });
      
      setCartItems(updatedItems);
      calculateTotal(updatedItems);
    } catch (err) {
      alert('Ошибка при обновлении количества');
    }
  };

  const removeItem = async (itemId) => {
    try {
      await axios.delete(`/api/cart/${itemId}`);
      const updatedItems = cartItems.filter(item => item._id !== itemId);
      setCartItems(updatedItems);
      calculateTotal(updatedItems);
    } catch (err) {
      alert('Ошибка при удалении товара');
    }
  };

  const checkout = async () => {
    try {
      await axios.post('/api/orders', {
        items: cartItems.map(item => ({
          partId: item.part._id,
          quantity: item.quantity
        }))
      });
      
      // Очистка корзины после успешного оформления
      setCartItems([]);
      setTotal(0);
      alert('Заказ успешно оформлен!');
    } catch (err) {
      alert('Ошибка при оформлении заказа');
    }
  };

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div className="alert alert-danger">{error}</div>;

  return (
    <div className="cart">
      <h2>Корзина</h2>
      
      {cartItems.length === 0 ? (
        <div className="empty-cart">
          <p>Ваша корзина пуста</p>
          <Link to="/catalog" className="btn btn-primary">
            Перейти в каталог
          </Link>
        </div>
      ) : (
        <>
          <div className="cart-items">
            {cartItems.map(item => (
              <div key={item._id} className="cart-item">
                <img
                  src={item.part.images[0]}
                  alt={item.part.name}
                  className="item-image"
                />
                
                <div className="item-details">
                  <Link to={`/parts/${item.part._id}`}>
                    <h3>{item.part.name}</h3>
                  </Link>
                  <p>{item.part.manufacturer}</p>
                  <p className="price">{item.part.price} руб.</p>
                </div>

                <div className="quantity-control">
                  <button
                    onClick={() => updateQuantity(item._id, item.quantity - 1)}
                    className="btn btn-secondary"
                  >
                    -
                  </button>
                  <span>{item.quantity}</span>
                  <button
                    onClick={() => updateQuantity(item._id, item.quantity + 1)}
                    className="btn btn-secondary"
                  >
                    +
                  </button>
                </div>

                <div className="item-total">
                  <p>{item.part.price * item.quantity} руб.</p>
                </div>

                <button
                  onClick={() => removeItem(item._id)}
                  className="btn btn-danger remove-item"
                >
                  Удалить
                </button>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <div className="summary-row">
              <span>Итого:</span>
              <span className="total">{total} руб.</span>
            </div>
            
            <button
              onClick={checkout}
              className="btn btn-primary checkout-button"
            >
              Оформить заказ
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default Cart;
