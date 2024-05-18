


// let urls = ['https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/age/latest.json',
// 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json'
// ]




// /** @type {import('./$types').PageLoad} */

// export const load = async ({ fetch }) => {

    // const fetchTop = async (urlo) => {
    //     const latestRes = await fetch(urlo)
    //     const latest = await latestRes.json()
    //     // .then(latest => {return latest})

    //         return { latest }

    // }

//     return {
//         'age': fetchTop('https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/age/latest.json')
//     }
// }



// export const load = async ({ fetch }) => {
//     const fetchTop = async () => {
//         const latestRes = await fetch(`https://dummyjson.com/quotes?limit=10`)
//         const latest = await latestRes.json()
    
//         return  latest.quotes 
    
//     }

// 	return { 
//         age: fetchTop() 
//     }
// }




// export async function load({ fetch }) {
// 	const ager = await fetch(`https://raw.githubusercontent.com/joshnicholas/Archives/main/Combined/top_stories.json`);
// 	const agel = await ager.json();

// 	return { agel};
// }