import React, { useState, useEffect } from 'react';
import { useAuth } from '../../context/AuthContext';
import axios from 'axios';

const Profile = () => {
  const { user } = useAuth();
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [profile, setProfile] = useState({
    name: user?.name || '',
    email: user?.email || '',
    phone: user?.phone || '',
    address: user?.address || ''
  });

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const res = await axios.get('/api/orders/my');
      setOrders(res.data);
      setLoading(false);
    } catch (err) {
      setError('Ошибка загрузки заказов');
      setLoading(false);
    }
  };

  const handleProfileUpdate = async (e) => {
    e.preventDefault();
    try {
      await axios.put('/api/users/profile', profile);
      alert('Профиль успешно обновлен');
    } catch (err) {
      setError('Ошибка обновления профиля');
    }
  };

  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value
    });
  };

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div className="alert alert-danger">{error}</div>;

  return (
    <div className="profile">
      <h2>Личный кабинет</h2>
      
      <div className="profile-section">
        <h3>Личные данные</h3>
        <form onSubmit={handleProfileUpdate}>
          <div className="form-group">
            <label htmlFor="name">Имя</label>
            <input
              type="text"
              id="name"
              name="name"
              value={profile.name}
              onChange={handleChange}
              className="form-control"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={profile.email}
              onChange={handleChange}
              className="form-control"
              readOnly
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="phone">Телефон</label>
            <input
              type="tel"
              id="phone"
              name="phone"
              value={profile.phone}
              onChange={handleChange}
              className="form-control"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="address">Адрес доставки</label>
            <textarea
              id="address"
              name="address"
              value={profile.address}
              onChange={handleChange}
              className="form-control"
            />
          </div>
          
          <button type="submit" className="btn btn-primary">
            Сохранить изменения
          </button>
        </form>
      </div>

      <div className="profile-section">
        <h3>История заказов</h3>
        {orders.length === 0 ? (
          <p>У вас пока нет заказов</p>
        ) : (
          <div className="orders-list">
            {orders.map(order => (
              <div key={order._id} className="order-card">
                <div className="order-header">
                  <span>Заказ #{order._id}</span>
                  <span className="order-date">
                    {new Date(order.createdAt).toLocaleDateString()}
                  </span>
                  <span className={`order-status status-${order.status}`}>
                    {order.status}
                  </span>
                </div>
                
                <div className="order-items">
                  {order.items.map(item => (
                    <div key={item._id} className="order-item">
                      <img
                        src={item.part.images[0]}
                        alt={item.part.name}
                        className="item-image"
                      />
                      <div className="item-details">
                        <h4>{item.part.name}</h4>
                        <p>Количество: {item.quantity}</p>
                        <p>Цена: {item.part.price} руб.</p>
                      </div>
                    </div>
                  ))}
                </div>
                
                <div className="order-footer">
                  <span>Итого: {order.total} руб.</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Profile;
