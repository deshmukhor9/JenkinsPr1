// // declarative method
// pipeline{
//     agent any
//     environment{
//         PYTHON = "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
//     }
//     triggers{
//         cron('*/2   *   *   *   *')
//     }
//     stages{
//         stage('Checkout code'){
//             steps{
//                 checkout scm
//             }
//         }
//         stage('Extract data'){
//             steps{
//                 bat "${env.PYTHON} extract.py"
//             }
//         }
//     }

// }


// // // scripted method
// // node{
// //     try{
// //         stage('Checkout code'){
// //             checkout scm
// //         }
// //         stage('Extract Data'){
// //             bat 'python extract.py'
// //         }
// //         }
// //     catch(err){
// //         echo "pipeline error: ${err}"
// //     }
// //     finally {
// //         echo "pipeline completed"
// //     }   
// // }


pipeline{
    agent any
    environment {
        PYTHON = 'C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }
    stages{
        stage('checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Extract data'){
            steps{
                bat "${env.PYTHON} -m pip install -r requirements.txt"
            }
        }
        stage('Extract Data'){
            steps{
                bat "${env.PYTHON} extract_from_api.py"
            }
        }
    }
}
