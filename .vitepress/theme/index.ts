// https://vitepress.dev/guide/custom-theme
import "@fontsource/noto-sans-jp/400.css";
import "@fontsource/noto-sans-jp/500.css";
import "@fontsource/noto-sans-mono/400.css";
import "@fontsource/noto-sans-mono/500.css";
import "virtual:uno.css";
import { EnhanceAppContext } from "vitepress";
import Theme from "vitepress/theme-without-fonts";
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
