import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: "ja-JP",
  title: "計算論的神経科学",
  titleTemplate: "Neuromatch Academy: Computational Neuroscience",
  description: "Neuromatch Academy:  Computational Neuroscience",
  lastUpdated: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "ホーム", link: "/" },
      { text: "講義一覧", link: "/tutorials/" },
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
    sidebar: {
      "/": [
        {
          items: [{ text: "Introduction", link: "/introduction" }],
        },
      ],
      "/tutorials/": [
        {
          text: "モデリング入門（Week1）",
          items: [
            {
              text: "モデルタイプ（Day1）",
              link: "/tutorials/w1/d1/",
              items: [
                { text: "Intro", link: "/tutorials/w1/d1/intro" },
                {
                  text: 'チュートリアル１："What" モデル',
                  link: "/tutorials/w1/d1/p1",
                },
                {
                  text: 'チュートリアル２："How" モデル',
                  link: "/tutorials/w1/d1/p2",
                },
                {
                  text: 'チュートリアル３："Why" モデル',
                  link: "/tutorials/w1/d1/p3",
                },
                {
                  text: "チュートリアル４：モデルに関するディスカッション",
                  link: "/tutorials/w1/d1/p4",
                },
                { text: "Outro", link: "/tutorials/w1/d1/outro" },
                { text: "参考文献", link: "/tutorials/w1/d1/further-readings" },
                { text: "まとめ", link: "/tutorials/w1/d1/summary" },
              ],
            },
          ],
        },
      ],
    },
  },
});
