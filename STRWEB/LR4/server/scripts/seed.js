require('dotenv').config();
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const User = require('../models/User');
const Category = require('../models/Category');
const Part = require('../models/Part');
const PromoCode = require('../models/PromoCode');

const categories = [
    {
        name: 'Двигатель и компоненты',
        description: 'Запчасти для двигателя и связанные компоненты',
        slug: 'engine'
    },
    {
        name: 'Тормозная система',
        description: 'Компоненты тормозной системы',
        slug: 'brakes'
    },
    {
        name: 'Подвеска',
        description: 'Детали подвески и амортизации',
        slug: 'suspension'
    },
    {
        name: 'Кузовные детали',
        description: 'Внешние элементы кузова',
        slug: 'body'
    },
    {
        name: 'Масла и жидкости',
        description: 'Технические жидкости и масла',
        slug: 'fluids'
    },
    {
        name: 'Шины и диски',
        description: 'Колёса и связанные компоненты',
        slug: 'wheels'
    },
    {
        name: 'Аксессуары',
        description: 'Дополнительное оборудование и аксессуары',
        slug: 'accessories'
    }
];

const parts = [
    {
        name: 'Свеча зажигания NGK',
        articleNumber: 'NGK-1234',
        description: 'Высококачественная свеча зажигания для бензиновых двигателей',
        price: 15.99,
        images: ['uploads/products/свеча_a.jpg', 'uploads/products/свеча_b.jpg'],
        categorySlug: 'engine',
        stock: 100
    },
    {
        name: 'Тормозной диск Brembo',
        articleNumber: 'BR-5678',
        description: 'Вентилируемый тормозной диск премиум качества',
        price: 89.99,
        images: ['uploads/products/тормозной_диск_a.jpg', 'uploads/products/тормозной_диск_b.jpg'],
        categorySlug: 'brakes',
        stock: 50
    },
    {
        name: 'Амортизатор KYB',
        articleNumber: 'KYB-9012',
        description: 'Газовый амортизатор для комфортной езды',
        price: 120.00,
        images: ['uploads/products/амортизатор_a.jpg', 'uploads/products/амортизатор_b.jpg'],
        categorySlug: 'suspension',
        stock: 30
    },
    {
        name: 'Передний бампер',
        articleNumber: 'BP-3456',
        description: 'Передний бампер с местами под противотуманные фары',
        price: 299.99,
        images: ['uploads/products/бампер_a.jpg', 'uploads/products/бампер_b.jpg'],
        categorySlug: 'body',
        stock: 15
    },
    {
        name: 'Моторное масло Castrol Edge',
        articleNumber: 'CO-7890',
        description: 'Синтетическое моторное масло 5W-40',
        price: 45.99,
        images: ['uploads/products/масло_a.jpg', 'uploads/products/масло_b.jpg'],
        categorySlug: 'fluids',
        stock: 200
    },
    {
        name: 'Летняя шина Michelin',
        articleNumber: 'MT-2345',
        description: 'Летняя шина 225/45 R17',
        price: 159.99,
        images: ['uploads/products/шина_a.jpg', 'uploads/products/шина_b.jpg'],
        categorySlug: 'wheels',
        stock: 40
    },
    {
        name: 'Воздушный фильтр K&N',
        articleNumber: 'KN-6789',
        description: 'Высокопроизводительный воздушный фильтр',
        price: 49.99,
        images: ['uploads/products/фильтр_a.jpg', 'uploads/products/фильтр_b.jpg'],
        categorySlug: 'engine',
        stock: 75
    },
    {
        name: 'Стартер Bosch',
        articleNumber: 'BS-1122',
        description: 'Надежный стартер для большинства моделей',
        price: 199.99,
        images: ['uploads/products/стартер_a.jpg', 'uploads/products/стартер_b.jpg'],
        categorySlug: 'engine',
        stock: 25
    },
    {
        name: 'Радиатор охлаждения',
        articleNumber: 'RD-3344',
        description: 'Алюминиевый радиатор охлаждения двигателя',
        price: 149.99,
        images: ['uploads/products/радиатор_a.jpg', 'uploads/products/радиатор_b.jpg'],
        categorySlug: 'engine',
        stock: 30
    },
    {
        name: 'Автомобильный держатель',
        articleNumber: 'AC-5566',
        description: 'Универсальный держатель для телефона',
        price: 24.99,
        images: ['uploads/products/аксессуар_a.jpg', 'uploads/products/аксессуар_b.jpg'],
        categorySlug: 'accessories',
        stock: 150
    }
];

const promoCodes = [
    {
        code: 'WELCOME2024',
        discount: 15,
        expirationDate: new Date('2024-12-31'),
        isActive: true
    },
    {
        code: 'SPRING20',
        discount: 20,
        expirationDate: new Date('2024-05-31'),
        isActive: true
    },
    {
        code: 'SUMMER10',
        discount: 10,
        expirationDate: new Date('2024-08-31'),
        isActive: true
    }
];

const admins = [
    {
        name: 'Admin User',
        email: 'admin@autoshop.com',
        password: 'admin123',
        role: 'admin',
        avatar: 'uploads/products/default-profile-picture.png'
    }
];

async function seedDatabase() {
    try {
        // Подключение к базе данных с дополнительными опциями
        await mongoose.connect('mongodb+srv://autoshop:password1525@cluster0.ctei9.mongodb.net/autoshop', {
            useNewUrlParser: true,
            useUnifiedTopology: true,
            retryWrites: true,
            w: 'majority',
            serverSelectionTimeoutMS: 5000,
            socketTimeoutMS: 45000,
        });
        console.log('Connected to MongoDB');

        // Очистка базы данных
        await Promise.all([
            Category.deleteMany({}),
            Part.deleteMany({}),
            PromoCode.deleteMany({}),
            User.deleteMany({ role: 'admin' })
        ]);

        // Создание категорий
        const createdCategories = await Category.insertMany(categories);
        console.log('Categories created');

        // Создание товаров
        const categoryMap = createdCategories.reduce((map, category) => {
            map[category.slug] = category._id;
            return map;
        }, {});

        const partsWithCategories = parts.map(part => ({
            ...part,
            category: categoryMap[part.categorySlug]
        }));

        await Part.insertMany(partsWithCategories);
        console.log('Parts created');

        // Создание промокодов
        await PromoCode.insertMany(promoCodes);
        console.log('Promo codes created');

        // Создание администраторов
        const hashedAdmins = await Promise.all(
            admins.map(async admin => ({
                ...admin,
                password: await bcrypt.hash(admin.password, 12)
            }))
        );
        await User.insertMany(hashedAdmins);
        console.log('Admins created');

        console.log('Database seeded successfully');
        process.exit(0);
    } catch (error) {
        console.error('Error seeding database:', error);
        process.exit(1);
    }
}

seedDatabase();
