<script>
    import * as d3 from 'd3';
    import { Styles,Input } from 'sveltestrap';

    import { onMount } from 'svelte';

    export let urlo

    // let keep = []
    // let data = d3.json(urlo)
    //   .then(response => {
  
    //     // console.log("response", response.items)

    //     keep = Object.values([... new Set(response.items.map(d =>d))])
  
    //   })

    //   onMount(d3.json(urlo)
    //   .then(response => {
  
    //     // console.log("response", response.items)

    //     keep = Object.values([... new Set(response.items.map(d =>d))])
  
    //   })
	// )

    let data 

    async function getData(urlo){
		let response = await fetch(urlo)
		let data = await response.json()
		console.log(data)
		return data
	}

    async function updateData(urlo) {
		data = await getData(urlo)		
	}

    //   $: console.log("keep: ", keep)

	$: updateData(urlo)

    // onMount(updateData(urlo))

    // data = await getData(urlo)
    $: console.log("data: ", data)
    $: console.log(typeof data)

      
</script>


<div class='container w-full'>

    {#key data}
        {#if data}

            {#each data.items as post}

            {post.content_html}
            
            <hr>

            {/each}

        {/if}
    {/key}
</div>