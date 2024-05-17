// import { posts } from '$lib/data/posts'

// /** @type {import('./$types').PageServerLoad} */
// export async function load() {
//   return {
//     posts: posts.slice(0, 5)
//   }
// }


// let urls = ['https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/age/latest.json',
// 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json'
// ]






// /** @type {import('./$types').PageLoad} */
// export async function load({ fetch }) 
// {   let items = {}
    
//     await Promise.all([1, 2, 3].map(id => 
//     fetch(`https://jsonplaceholder.typicode.com/todos/${id}`).then(resp => items[id] = resp.json())
//   ))
  
// //   return {items}

//   console.log(items)
//     }

// /** @type {import('./$types').PageLoad} */
// export async function load({ fetch }) 
// {	
//     const res = await fetch(`https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/feed/latest.json`);	
// const item = await res.json();
// return { item };}