<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="login()">
      Log In
    </button>
    <br>
    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="logout()">
      Log Out
    </button>
    <br>
    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="patientRecords()">
      List Patient Records
    </button>
    <br>
    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="users()">
      List Users
    </button>
    <br>
    {{ message }}
    <br>
  </div>

</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'

const API_URL = 'http://localhost:3000'
const auth = new AuthService()

export default {
  name: 'App',
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: '',
      user: ''
    }
  },
  methods: {
    // this method calls the AuthService user() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
      this.message = ''
      this.user = ''
    },
    patientRecords () {
      const url = `${API_URL}/patient-record/?format=json`
      return axios.get(url, {headers: {Authorization: `Bearer ${AuthService.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    },
    users () {
      const url = `${API_URL}/user/?format=json`
      return axios.get(url, {headers: {Authorization: `Bearer ${AuthService.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}

</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
