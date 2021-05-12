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
            <div class="mb-3">
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Recherche" v-model="form.search_text" required>
            </div>
            <h5 class="font-bold">Requête initale :</h5>
            <div class="mb-3">
                <label for="range-jdd-title" class="form-label">Pertinence du titre du jeu de données</label>
                <input type="range" class="form-range" id="range-jdd-title" v-model="form.boost_dataset_title">
            </div>
            <div class="mb-3">
                <label for="range-jdd-desc" class="form-label">Pertinence de la description du jeu de données</label>
                <input type="range" class="form-range" id="range-jdd-desc" v-model="form.boost_dataset_description">
            </div>
            <div class="mb-3">
                <label for="range-org-title" class="form-label">Pertinence du titre de l'organisation émétrice du jeu de données</label>
                <input type="range" class="form-range" id="range-org-title" v-model="form.boost_org_title">
            </div>
            <h5 class="font-bold">Post-traitement :</h5>
            <div class="mb-3">
                <label for="range-jdd-featured" class="form-label">Poids de l'attribut "mis en avant" du jeu de données (featured)</label>
                <input type="range" class="form-range" id="range-jdd-featured" v-model="form.weight_dataset_featured">
            </div>
            <div class="mb-3">
                <label for="range-org-public" class="form-label">Poids de la présence du badge "service public" de l'organisation émétrice du jeu de données</label>
                <input type="range" class="form-range" id="range-org-public" v-model="form.weight_org_public_service">
            </div>
            <div class="mb-3">
                <label for="range-org-badge" class="form-label">Poids de la typologie de l'organisation émétrice du jeu de données</label>
                <input type="range" class="form-range" id="range-org-badge" v-model="form.weight_org_badge">
            </div>
            <button type="submit" class="btn btn-primary">Valider</button>
        </form>
    </div>
    <div class="md:max-w-screen-lg mx-auto mt-16">
        <div v-for="result in resultList" :key="result.id">
            <div class="relative py-3 md:max-w-screen-lg md:mx-auto">
                <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl">
                    <div class="max-w-4xl mx-auto">
                        <p class="text-xs text-gray-500">{{ result.source.organization_name }}</p>
                        <p class="text-4xl mt-4">{{ result.source.title }}</p>
                    <div class="divide-y divide-gray-200">
                        <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                            <p>{{ result.source.description }}</p>
                        </div>
                        <div class="pt-6 text-base leading-6 font-bold sm:text-lg sm:leading-7">
                            <div>
                                <!-- Button trigger modal -->
                                <div class="btn-group">
                                    <a class="btn btn-primary" :href="result.source.url" role="button">Lien DGF</a>
                                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="`#modal-result-${result.source.remote_id}`">
                                        Explication
                                    </button>
                                </div>
                                <!-- Modal -->
                                <div class="modal fade" :id="`modal-result-${result.source.remote_id}`" tabindex="-1" :aria-labelledby="`modal-result-${result.source.remote_id}-Label`" aria-hidden="true">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" :id="`modal-result-${result.source.remote_id}-Label`">{{ result.source.title }}</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <div class="modal-body">
                                                <div class="mb-3">
                                                    <h5>Infos :</h5>
                                                    <p>Jeu de données mis en avant : {{ result.source.featured }}</p>
                                                    <div v-for="badge in result.source.organization_badges" :key="badge.id">
                                                        <span class="badge rounded-pill bg-secondary">{{ badge }}</span>
                                                    </div>
                                                </div>
                                                <hr>
                                                <div class="mt-3 mb-2">
                                                    <h5>Explain :</h5>
                                                    <code>{{ result.explain }}</code>
                                                </div>
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
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
        weight_dataset_featured: 1,
        weight_org_public_service: 1,
        weight_org_badge: 1
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
