// https://vitepress.dev/guide/custom-theme
import { EnhanceAppContext } from "vitepress";
import Theme from "vitepress/theme";
import "./style.css";

import Layout from "./Layout.vue";
import YouTube from "./YouTube.vue";

export default {
  extends: Theme,
  Layout,
  enhanceApp({ app, router, siteData }: EnhanceAppContext) {
    app.component("YouTube", YouTube);
  },
};
