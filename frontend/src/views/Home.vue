<template>
  <div class="home">
    <header role="banner" class="fr-header">
      <div class="fr-header__body">
        <div class="fr-container">
          <div class="fr-header__body-row">
            <div class="fr-header__brand fr-enlarge-link">
              <div class="fr-header__brand-top">
                <div class="fr-header__logo">
                  <a href="/" title="Accueil">
                    <p class="fr-logo">République<br>française</p>
                  </a>
                </div>
              </div>
            </div>
            <div class="fr-header__service">
              <a href="/" title="Support">
                  <p class="fr-header__service-title">Recherche data.gouv.fr</p>
              </a>
              <p class="fr-header__service-tagline">Preuve de concept</p>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="md:max-w-screen-md mx-auto mt-16">
      <form v-on:submit.prevent="checkForm" id="search-form">
        <div class="fr-search-bar" id="header-search" role="search">
            <label class="fr-label" for="search-784-input">
                Recherche
            </label>
            <input class="fr-input" placeholder="Rechercher" type="search" id="search-784-input" name="search-784-input" v-model="form.search_text">
        </div>
        <div class="mt-6 font-bold">Requête initiale :</div>
        <div class="mt-2 fr-form-group">
            <fieldset class="fr-fieldset fr-fieldset--inline">
                <legend class="fr-fieldset__legend fr-text--regular" id='radio-jdd-title-legend'>
                    Pertinence du titre du jeu de données
                </legend>
                <div class="fr-fieldset__content">
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-1" name="radio-jdd-title" value="1" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-1">1</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-2" name="radio-jdd-title" value="2" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-2">2</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-3" name="radio-jdd-title" value="3" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-3">3</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-4" name="radio-jdd-title" value="4" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-4">4</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-5" name="radio-jdd-title" value="5" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-5">5</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-6" name="radio-jdd-title" value="6" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-6">6</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-7" name="radio-jdd-title" value="7" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-7">7</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-8" name="radio-jdd-title" value="8" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-8">8</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-9" name="radio-jdd-title" value="9" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-9">9</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-title-10" name="radio-jdd-title" value="10" v-model="form.boost_dataset_title">
                        <label class="fr-label" for="radio-jdd-title-10">10</label>
                    </div>
                </div>
            </fieldset>
        </div>
        <div class="fr-form-group">
            <fieldset class="fr-fieldset fr-fieldset--inline">
                <legend class="fr-fieldset__legend fr-text--regular" id='radio-jdd-desc-legend'>
                    Pertinence de la description du jeu de données
                </legend>
                <div class="fr-fieldset__content">
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-1" name="radio-jdd-desc" value="1" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-1">1</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-2" name="radio-jdd-desc" value="2" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-2">2</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-3" name="radio-jdd-desc" value="3" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-3">3</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-4" name="radio-jdd-desc" value="4" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-4">4</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-5" name="radio-jdd-desc" value="5" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-5">5</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-6" name="radio-jdd-desc" value="6" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-6">6</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-7" name="radio-jdd-desc" value="7" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-7">7</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-8" name="radio-jdd-desc" value="8" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-8">8</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-9" name="radio-jdd-desc" value="9" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-9">9</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-desc-10" name="radio-jdd-desc" value="10" v-model="form.boost_dataset_description">
                        <label class="fr-label" for="radio-jdd-desc-10">10</label>
                    </div>
                </div>
            </fieldset>
        </div>
        <div class="fr-form-group">
            <fieldset class="fr-fieldset fr-fieldset--inline">
                <legend class="fr-fieldset__legend fr-text--regular" id='radio-org-title-legend'>
                    Pertinence du titre de l'organisation émétrice du jeu de données
                </legend>
                <div class="fr-fieldset__content">
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-1" name="radio-org-title" value="1" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-1">1</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-2" name="radio-org-title" value="2" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-2">2</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-3" name="radio-org-title" value="3" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-3">3</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-4" name="radio-org-title" value="4" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-4">4</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-5" name="radio-org-title" value="5" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-5">5</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-6" name="radio-org-title" value="6" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-6">6</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-7" name="radio-org-title" value="7" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-7">7</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-8" name="radio-org-title" value="8" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-8">8</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-9" name="radio-org-title" value="9" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-9">9</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-title-10" name="radio-org-title" value="10" v-model="form.boost_org_title">
                        <label class="fr-label" for="radio-org-title-10">10</label>
                    </div>
                </div>
            </fieldset>
        </div>
        <div class="font-bold">Post traitement du score :</div>
        <div class="mt-2 fr-form-group">
            <fieldset class="fr-fieldset fr-fieldset--inline">
                <legend class="fr-fieldset__legend fr-text--regular" id='radio-jdd-featured-legend'>
                    Poids de l'attribut "mis en avant" du jeu de données (featured)
                </legend>
                <div class="fr-fieldset__content">
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-1" name="radio-jdd-featured" value="1" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-1">1</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-2" name="radio-jdd-featured" value="2" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-2">2</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-3" name="radio-jdd-featured" value="3" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-3">3</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-4" name="radio-jdd-featured" value="4" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-4">4</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-5" name="radio-jdd-featured" value="5" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-5">5</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-6" name="radio-jdd-featured" value="6" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-6">6</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-7" name="radio-jdd-featured" value="7" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-7">7</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-8" name="radio-jdd-featured" value="8" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-8">8</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-9" name="radio-jdd-featured" value="9" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-9">9</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-jdd-featured-10" name="radio-jdd-featured" value="10" v-model="form.weight_dataset_featured">
                        <label class="fr-label" for="radio-jdd-featured-10">10</label>
                    </div>
                </div>
            </fieldset>
        </div>
        <div class="fr-form-group">
            <fieldset class="fr-fieldset fr-fieldset--inline">
                <legend class="fr-fieldset__legend fr-text--regular" id='radio-org-badge-legend'>
                    Poids de la présence du badge "service public" de l'organisation émétrice du jeu de données
                </legend>
                <div class="fr-fieldset__content">
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-1" name="radio-org-badge" value="1" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-1">1</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-2" name="radio-org-badge" value="2" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-2">2</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-3" name="radio-org-badge" value="3" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-3">3</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-4" name="radio-org-badge" value="4" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-4">4</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-5" name="radio-org-badge" value="5" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-5">5</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-6" name="radio-org-badge" value="6" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-6">6</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-7" name="radio-org-badge" value="7" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-7">7</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-8" name="radio-org-badge" value="8" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-8">8</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-9" name="radio-org-badge" value="9" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-9">9</label>
                    </div>
                    <div class="fr-radio-group">
                        <input type="radio" id="radio-org-badge-10" name="radio-org-badge" value="10" v-model="form.weight_org_badge">
                        <label class="fr-label" for="radio-org-badge-10">10</label>
                    </div>
                </div>
            </fieldset>
        </div>
        <button class="fr-btn" type="submit">Valider</button>
      </form>
    </div>
    <div class="md:max-w-screen-lg mx-auto mt-16">
      <div v-for="result in resultList" :key="result.id">
        <div class="fr-card fr-card--horizontal fr-enlarge-link mb-6">
          <div class="fr-card__body">
            <p class="fr-card__detail">{{ result.source.organization_name }}</p>
            <h4 class="fr-card__title">
                <a :href="result.source.url" class="fr-card__link">{{ result.source.title }}</a>
            </h4>
            <p class="fr-card__desc">{{ result.source.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

const API_HOST = process.env.NODE_ENV === 'production' ? '' : 'http://localhost:5000'

export default {
  name: 'Home',
  data () {
    return {
      form: {
        search_text: null,
        boost_dataset_title: 1,
        boost_dataset_description: 1,
        boost_org_title: 1,
        weight_dataset_featured: 10,
        weight_org_badge: 2
      },
      resultList: []
    }
  },
  methods: {
    async checkForm () {
      try {
        const response = await axios.post(`${API_HOST}/api`, this.form)
        this.resultList = response.data.results
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>
