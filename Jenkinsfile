// declarative method
// pipeline{
//     agent any
//     environment{
//         PYTHON = "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
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


// scripted method
node{
    try{
        stage('Checkout code'){
            checkout scm
        }
        stage('Extract Data'){
            bat 'python extract.py'
        }
        }
    catch(err){
        echo "pipeline error: ${err}"
    }
    finally {
        echo "pipeline completed"
    }   
}