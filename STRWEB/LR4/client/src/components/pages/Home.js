import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const Home = () => {
  const { isAuthenticated, user } = useAuth();

  return (
    <div className="home">
      <div className="hero">
        <h1>Добро пожаловать в AutoShop</h1>
        <p>Ваш надежный поставщик автозапчастей</p>
        
        {isAuthenticated ? (
          <div className="welcome-user">
            <h2>Здравствуйте, {user.name}!</h2>
            <div className="user-actions">
              <Link to="/catalog" className="btn btn-primary">
                Перейти в каталог
              </Link>
              <Link to="/cart" className="btn btn-secondary">
                Моя корзина
              </Link>
            </div>
          </div>
        ) : (
          <div className="guest-welcome">
            <h2>Присоединяйтесь к нам</h2>
            <p>Зарегистрируйтесь, чтобы получить доступ к полному функционалу магазина</p>
            <div className="auth-buttons">
              <Link to="/register" className="btn btn-primary">
                Регистрация
              </Link>
              <Link to="/login" className="btn btn-secondary">
                Войти
              </Link>
            </div>
          </div>
        )}
      </div>

      <div className="features">
        <div className="feature-card">
          <h3>Широкий выбор</h3>
          <p>Тысячи запчастей для различных марок автомобилей</p>
        </div>
        <div className="feature-card">
          <h3>Гарантия качества</h3>
          <p>Только оригинальные запчасти и надежные аналоги</p>
        </div>
        <div className="feature-card">
          <h3>Быстрая доставка</h3>
          <p>Доставка по всей стране в кратчайшие сроки</p>
        </div>
      </div>
    </div>
  );
};

export default Home;
