module.exports = {
  client: {
    service: {
      name: 'schirus',
      // URL to the GraphQL API
      url: 'http://localhost:8000/',
    },
    // Files processed by the extension
    includes: [
      'src/**/*.vue',
      'src/**/*.js',
    ],
  },
}