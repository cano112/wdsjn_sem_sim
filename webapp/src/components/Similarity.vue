<template>
  <div class="container-fluid">
    <div class="loading-overlay d-flex align-items-center justify-content-center"
         v-if="showLoading">
      <BSpinner label="Loading..." style="width: 6rem; height: 6rem;"></BSpinner>
    </div>
    <b-alert dismissible v-model="error" variant="warning">
      {{errorMessage}}
    </b-alert>
    <div class="row">
      <div class="col-12">
        <b-form @submit="onSubmit">
          <b-form-group
              id="sentence1-group"
              label="Zdanie pierwsze"
              label-for="sentence1">
            <b-form-input v-model="sentence1">
            </b-form-input>
          </b-form-group>

          <b-form-group
              id="sentence2-group"
              label="Zdanie drugie"
              label-for="sentence2">
            <b-form-input v-model="sentence2">
            </b-form-input>
          </b-form-group>

          <b-button type="submit"
                    v-if="sentence1 && sentence2 && !error"
                    onclick=""
                    variant="primary">
            Oblicz
          </b-button>
        </b-form>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <GChart
            v-if="results"
            type="BarChart"
            :data="results"
            :options="chartOptions"
        />
      </div>
    </div>
  </div>
</template>

<style>
  .loading-overlay {
    opacity: 0.5;
    background: #000;
    width: 100%;
    height: 100%;
    z-index: 10;
    top: 0;
    left: 0;
    position: fixed;
  }
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      chartOptions: {
        title: 'Semantic Similarity Index (%)',
        height: 450,
        legend: {
          position: 'none',
        },
        vAxis: {
          textPosition: 'in',
        },
      },
      sentence1: null,
      sentence2: null,
      algorithms: 'wmd,jaccard,cosine,sif_cosine,ensemble',
      results: null,
      showLoading: false,
      errorMessage: null,
      error: false,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      // eslint-disable-next-line no-console
      this.showLoading = true;
      axios.get(`http://${process.env.VUE_APP_HOST}:5000/similarity`, {
        params: {
          s1: this.sentence1,
          s2: this.sentence2,
          algorithms: this.algorithms,
        },
      }).then((res) => {
        this.showLoading = false;
        this.results = res.data;
      }).catch((error) => {
        this.showLoading = false;
        this.error = true;
        this.errorMessage = error.response.data;
      });
    },
  },
};
</script>
