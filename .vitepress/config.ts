import mathjax3 from "markdown-it-mathjax3";
import Unocss from "unocss/vite";
import { defineConfig } from "vitepress";

const customElements = ["mjx-container"];

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: "ja-JP",
  title: "計算論的神経科学",
  titleTemplate: "Neuromatch Academy: Computational Neuroscience",
  description: "Neuromatch Academy: Computational Neuroscience",
  lastUpdated: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "ホーム", link: "/" },
      { text: "講義一覧", link: "/tutorials/" },
      { text: "翻訳", link: "/members" },
    ],
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/FujishigeTemma/course-content-jp",
      },
    ],
    search: {
      provider: "local",
    },
    editLink: {
      pattern:
        "https://github.com/FujishigeTemma/course-content-jp/blob/main/:path",
    },
    sidebar: {
      "/": [
        {
          items: [
            { text: "Introduction", link: "/introduction" },
            {
              text: "前提知識と準備資料",
              link: "/prereqs",
            },
          ],
        },
      ],
      "/tutorials/": [
        {
          text: "W0：事前準備",
          collapsed: true,
          items: [
            {
              text: "W0D1：Pythonワークショップ1",
              collapsed: true,
              link: "/tutorials/w0/d1/",
              items: [
                {
                  text: "チュートリアル：LIFニューロン Part1",
                  link: "/tutorials/w0/d1/p1",
                },
              ],
            },
            {
              text: "W0D2：Pythonワークショップ2",
              collapsed: true,
              link: "/tutorials/w0/d2/",
              items: [
                {
                  text: "チュートリアル：LIFニューロン Part2",
                  link: "/tutorials/w0/d2/p1",
                },
              ],
            },
          ],
        },
        {
          text: "W1,W2：モデリング入門",
          collapsed: true,
          items: [
            {
              text: "W1D1：モデルタイプ",
              collapsed: true,
              link: "/tutorials/w1/d1/",
              items: [
                { text: "Intro", link: "/tutorials/w1/d1/intro" },
                {
                  text: 'チュートリアル1："What" モデル',
                  link: "/tutorials/w1/d1/p1",
                },
                {
                  text: 'チュートリアル2："How" モデル',
                  link: "/tutorials/w1/d1/p2",
                },
                {
                  text: 'チュートリアル3："Why" モデル',
                  link: "/tutorials/w1/d1/p3",
                },
                {
                  text: "チュートリアル4：モデルに関するディスカッション",
                  link: "/tutorials/w1/d1/p4",
                },
                { text: "Outro", link: "/tutorials/w1/d1/outro" },
                { text: "参考文献", link: "/tutorials/w1/d1/further-readings" },
                { text: "まとめ", link: "/tutorials/w1/d1/summary" },
              ],
            },
            {
              text: "W2D1：実践モデリング",
              collapsed: true,
              link: "/tutorials/w2/d1/",
              items: [
                { text: "Intro", link: "/tutorials/w2/d1/intro" },
                {
                  text: "チュートリアル1：問いの設計",
                  link: "/tutorials/w2/d1/p1",
                },
                { text: "Outro", link: "/tutorials/w2/d1/outro" },
                { text: "まとめ", link: "/tutorials/w2/d1/summary" },
              ],
            },
          ],
        },
        {
          text: "ニューロンモデル",
        },
      ],
    },
  },
  vite: {
    plugins: [Unocss()],
  },
  markdown: {
    config: (md) => {
      md.use(mathjax3);
    },
  },
  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => customElements.includes(tag),
      },
    },
  },
});
