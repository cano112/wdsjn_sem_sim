import Vue from 'vue';
import VueRouter from 'vue-router';
import Similarity from '../components/Similarity.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Semantic Similarity',
    component: Similarity,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
