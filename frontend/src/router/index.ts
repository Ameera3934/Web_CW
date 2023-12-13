import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../pages/MainPage.vue';
import OtherPage from '../pages/OtherPage.vue';
import LoginPage from '../pages/LoginPage.vue';
import RegisterPage from '../pages/RegisterPage.vue'; 

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : '';

const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'main-page', component: MainPage },
        { path: '/other', name: 'other-page', component: OtherPage },
        { path: '/login', name: 'login', component: LoginPage },
        { path: '/register', name: 'register', component: RegisterPage },
    ]
})

export default router;
