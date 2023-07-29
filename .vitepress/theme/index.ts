// https://vitepress.dev/guide/custom-theme
import { EnhanceAppContext } from "vitepress";
import Theme from "vitepress/theme";
import "./style.css";

import YouTube from "../components/YouTube.vue";
import Layout from "./Layout.vue";

export default {
  extends: Theme,
  Layout,
  enhanceApp({ app, router, siteData }: EnhanceAppContext) {
    app.component("YouTube", YouTube);
  },
};
