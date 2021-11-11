import '@fortawesome/fontawesome-free/css/all.css'
import '@/scss/app.scss'
import 'bootstrap'

import axios from 'axios'

import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css'

import { createApp } from 'vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
loadProgressBar()

createApp({}).use(store).use(router).mount('#app')
