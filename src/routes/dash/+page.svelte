<script>
  import { name } from '$lib/info.js'
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  import WikiTable from '$lib/components/wiki_table.svelte'
  import GoogleTable from '$lib/components/google_table.svelte'
  import TopTable from '$lib/components/top_stories_table.svelte'
  // import PostsList from '$lib/components/ScribblesList.svelte'

//   const urls = ["https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/abc_top/latest.json",
// "https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json",
// "https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/sbs_top/latest.json"];

// let response


// onMount(() => {

//   let datah = []

//   urls.forEach(urlo => {

//     d3.json(urlo)

//     .then(response => {
      
//     // console.log("Response: ", response)

//     datah.push(...response);


// })

//   })
  
//   console.log("Datah: ", datah)
// })

let datah = []
let groups = []
let keys
let colours

// let data = d3.json('https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/headlines/latest.json')
// .then(response => {

//   datah = [...response]
//   console.log("datah: ", datah)

//   datah.forEach(row => {
//     groups.push(row['Matches'])
//   })

//   console.log("Groups: ", groups)

//   colours = d3.scaleOrdinal().domain(groups)
//       .range(d3.schemeTableau10)
    
//   keys = Object.keys(datah[0])
//   console.log("Keys: ", keys)
// })


  /** @type {import('./$types').PageData} */


</script>

<svelte:head>
  <title>{name}</title>
</svelte:head>




<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

  <h1>ABC Top Stories</h1>
<TopTable urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/abc_top/latest.json'}/>

</div>

<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

  <h1>SBS Top Stories</h1>
<TopTable urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/sbs_top/latest.json'}/>

</div>


<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

  <h1>Guardian Top Stories</h1>
<TopTable urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json'}/>

</div>

<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

  <h1>Tech Meme Top Stories</h1>
<TopTable urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/tech_meme_top/latest.json'}/>

</div>

<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

  <h1>Top 1000 pages on Wikipedia</h1>
<WikiTable urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/wiki/latest.json'}/>

</div>


<div class="container flex flex-col flex-grow max-w-4xl mx-auto">

<h1>Top 20 trending on Google</h1>
  <GoogleTable urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google/latest.json'}/>

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



