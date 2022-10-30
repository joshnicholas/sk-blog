<script>
	import { onMount } from "svelte"
	import * as d3 from "d3"
	let data
 	onMount(
		async () => {
			data = await d3.csv('https://raw.githubusercontent.com/joshnicholas/cse_scrape/main/cse.csv')
		}
	)
	$: console.log(data)
</script>