<script>
  import { name } from '$lib/info.js'
  import { onMount } from 'svelte';
  import Table from '$lib/components/table.svelte'

let datah = []
let groups = []
let colours

  /** @type {import('./$types').PageData} */


</script>

<svelte:head>
  <title>{name}</title>
</svelte:head>

<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

<Table thingo={"Gnews"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Google News top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google_top/latest.json'}/>



<Table thingo={"ABC"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'ABC top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/abc_top/latest.json'}/>


<Table thingo={"SBS"}  standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'SBS top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/sbs_top/latest.json'}/>


<Table thingo={"Graun"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Guardian top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json'}/>



<Table thingo={"Techmem"}  standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Tech Meme top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/tech_meme_top/latest.json'}/>



<Table thingo={"Wiki"}  standfirst={"This data is only updated once per day. Special Wikipedia pages (search page, main page etc.) have been removed, so some page ranks will be missing. "} removeCol={"Page"} keys={["Page",'Rank', ]} title = {'Top 1000 trending on Wikipedia'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/wiki/latest.json'}/>



<Table thingo={"Gtrends"}  standfirst={""} removeCol={"Search"} keys={["Search","Rank"]} title = {'Top 20 Google searches'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google/latest.json'}/>

</div>

<style>
  /* a {
    @apply flex items-center gap-2 font-medium text-zinc-700;
  } */

  :global(.dark) a {
    @apply text-zinc-300;
  }

  ul {
  list-style-type: circle;
  font-size: 0.8em;
}

.container {
  margin-top: 10px;
}

.container h1{
  margin-top: 20px;
  margin-bottom: 10px;
  text-align: center;
  font-size: 2em;
}
</style>



