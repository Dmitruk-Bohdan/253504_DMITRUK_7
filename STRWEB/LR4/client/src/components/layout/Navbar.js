import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import '../../styles/Navbar.css';

const Navbar = () => {
    const { isAuthenticated, user, logout } = useAuth();
    const location = useLocation();

    const isActive = (path) => {
        return location.pathname === path ? 'active' : '';
    };

    const authLinks = (
        <>
            <li>
                <Link to="/profile" className={`nav-link ${isActive('/profile')}`}>
                    {user?.name}
                </Link>
            </li>
            <li>
                <Link to="/cart" className={`nav-link ${isActive('/cart')}`}>
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
                <Link to="/login" className={`nav-link ${isActive('/login')}`}>
                    Войти
                </Link>
            </li>
            <li>
                <Link to="/register" className={`nav-link ${isActive('/register')}`}>
                    Регистрация
                </Link>
            </li>
        </>
    );

    return (
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-brand">
                    AutoShop
                </Link>
                <ul className="nav-links">
                    <li>
                        <Link to="/" className={`nav-link ${isActive('/')}`}>
                            Главная
                        </Link>
                    </li>
                    <li>
                        <Link to="/catalog" className={`nav-link ${isActive('/catalog')}`}>
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
