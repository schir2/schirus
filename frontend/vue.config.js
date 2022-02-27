module.exports = {
  css: {
    loaderOptions: {
      sass: {
        additionalData: `
          @import "@/scss/variables.scss";
          @import "@/scss/mixins.scss";
        `,
      },
    },
  },
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].template = "./src/public/index.html";
      return args;
    });
  },
};
