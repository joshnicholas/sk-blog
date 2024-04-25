<script>
    import * as d3 from 'd3';
    // import { Styles,Input } from 'sveltestrap';
    export let recents

    import { onMount } from 'svelte';
    // export let urlo



  //   let recents = []
  //   let keep = []

  //   onMount(async () => {
  //       let data = d3.json(urlo)
  //     .then(response => {
  
  //       // console.log("response", response)
  //       //   keep = response.map(d => d)
  //         response.forEach(function(value, index, array) {

  //       // value['Search_var'] = Object.values(value).join(" ")
  //       keep.push(value)
  //         })

  //         recents = keep.map(d => d)
  
  //     })
	// });




    // let data = d3.json(urlo)
    //   .then(response => {
  
    //     console.log("response", response)
    //     //   keep = response.map(d => d)
    //       response.forEach(function(value, index, array) {

    //     // value['Search_var'] = Object.values(value).join(" ")
    //     keep.push(value)
    //       })

    //       recents = keep.map(d => d)
  
    //   })

// console.log("recents: ", recents)

let renamo = {"Scribbles": "Scribble", "Micro blog": "Post", "Article": "Article", "linklog":"Read"}
let colours = {"Scribbles": '#FF9700', "Article": "#30B0FF", "linklog": "#D61D1D"}
      
</script>


<div class='container w-full pb-20 text-center justify-center'>

    {#each recents as row}
    <li class='text-left py-4 justify-center mx-auto'>
        <a href='{row.Url}' target="_blank" style="color:{colours[row.Category]}" class='font-semibold'>{renamo[row.Category]}:</a>
        {row.Headline}
         <!-- - <a href='{row.Url}' class='font-semibold'>Source</a> -->
    </li>
    {/each}
</div>

<!-- <style>
    a {
      color: #FF9700
    }
  
    /* :global(.dark) a {
      @apply text-zinc-300;
    } */
  </style> -->