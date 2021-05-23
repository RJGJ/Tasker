chainWebpack: (config) => {
  config.optimization.delete("splitChunks");
};
