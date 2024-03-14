pipeline {
    agent {label "shared-agent" }
    options {
        durabilityHint('PERFORMANCE_OPTIMIZED')
        ansiColor('xterm')
        timestamps()
        buildDiscarder logRotator(artifactDaysToKeepStr: '14', artifactNumToKeepStr: '', daysToKeepStr: '14', numToKeepStr: '')
        skipStagesAfterUnstable()
        parallelsAlwaysFailFast()
        disableConcurrentBuilds()
    }
    // set env for conda
    environment {
    PATH = "${tool 'Conda'}:${env.WORKSPACE}/.condaenv/bin:${PATH}"
    CONDA_ENV_PATH = "${env.WORKSPACE}/.condaenv"
    HOME_DIR = "${env.WORKSPACE}"
    // get AIM_API endpoint from jenkins build params
    AIM_API_HOST = "${env.AIM_API_HOST}"
    }
    stages {
            stage ('Spin up cotainer')
            {
                steps {
                     withCredentials([[
                      credentialsId: 'AIM_CREDENTIALS',
                      userVariable: 'AIM_USER',
                      passwordVariable: 'AIM_PASSWORD']]){
                        script {
                            def dockerImage="s.dock.host.com/aim-performance:current"
                            docker.image(dockerImage).inside('-u 0:0 -e AIM_API_HOST=${AIM_API_HOST} -e AIM_USER=${AIM_USER}' -e AIM_PASSWORD=${AIM_PASSWORD}) {
                            sh """
                            bash -c "multimech-run aim_api_login_perf"
                            """
                        }
                    }
                }
            }
            }
    }

     post {
         failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>
                         """,
                to: 'dan.bordeanu@host.com'
            )
        }
        success {
              emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>
                         """,
                to: 'dan.bordeanu@host.com'
            )
         }
    }
}
