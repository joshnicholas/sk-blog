// import { posts } from '$lib/data/posts'

// /** @type {import('./$types').PageServerLoad} */
// export async function load() {
//   return {
//     posts: posts.slice(0, 5)
//   }
// }


/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) 
{	const res = await fetch(`https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/feed/latest.json`);	
const item = await res.json();
return { item };}