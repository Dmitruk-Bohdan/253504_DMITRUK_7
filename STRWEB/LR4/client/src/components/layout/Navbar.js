import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const Navbar = () => {
  const { isAuthenticated, user, logout } = useAuth();

  const authLinks = (
    <>
      <li>
        <Link to="/profile" className="nav-link">
          {user?.name}
        </Link>
      </li>
      <li>
        <Link to="/cart" className="nav-link">
          Корзина
        </Link>
      </li>
      <li>
        <a href="#!" onClick={logout} className="nav-link">
          Выйти
        </a>
      </li>
    </>
  );

  const guestLinks = (
    <>
      <li>
        <Link to="/login" className="nav-link">
          Войти
        </Link>
      </li>
      <li>
        <Link to="/register" className="nav-link">
          Регистрация
        </Link>
      </li>
    </>
  );

  return (
    <nav className="navbar">
      <div className="container navbar-container">
        <Link to="/" className="navbar-brand">
          AutoShop
        </Link>
        <ul className="nav-links">
          <li>
            <Link to="/" className="nav-link">
              Главная
            </Link>
          </li>
          <li>
            <Link to="/catalog" className="nav-link">
              Каталог
            </Link>
          </li>
          {isAuthenticated ? authLinks : guestLinks}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
