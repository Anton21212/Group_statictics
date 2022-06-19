from decohints import decohints

from .errors import *


@decohints
def check_vk_api_response_for_errors(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)

        if 'response' in result:
            print("OK")
            return result

        error_code = result['error']['error_code']
        error_msg = result['error']['error_msg']
        error_request_params = result['error']['request_params']

        if error_code == 214:
            raise AccessToAddingPostDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 1:
            raise UnknownErrorHasOccurred(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 2:
            raise TheApplicationIsDisabled(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 3:
            raise UnknownMethodPassed(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 4:
            raise InvalidSignature(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 5:
            raise UserAuthorizationFailed(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 6:
            raise TooManyRequestsPerSecond(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 7:
            raise YouDoNotHavePermissionToPerformThisAction(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 8:
            raise InvalidRequest(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 9:
            raise TooManySimilarActions(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 10:
            raise AnInternalServerErrorHasOccurred(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 11:
            raise InTestModeTheApplicationMustBeTurnedOffOrTheUserMustBeLoggedIn(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 14:
            raise YouNeedToEnterTheCodeFromTheImageCaptcha(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 15:
            raise AccessIsDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 16:
            raise RequestsMustBeMadeOverHTTPSBecauseTheUserHasEnabledASettingThatRequiresWorkOverASecureConnection(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 17:
            raise UserValidationRequired(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 18:
            raise UserWasDeletedOrBanned(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 19:
            raise ContentBlocked(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 20:
            raise ThisActionIsProhibitedForNonStandaloneApplications(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 21:
            raise ThisActionIsAllowedOnlyForStandaloneAndOpenAPIApplications(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 23:
            raise TheMethodHasBeenDisabled(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 24:
            raise UserConfirmationRequired(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 27:
            raise TheCommunityAccessKeyIsInvalid(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 28:
            raise TheApplicationAccessKeyIsInvalid(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 29:
            raise QuantityLimitPerMethodCallReached(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 30:
            raise ProfileIsPrivate(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 100:
            raise OneOfTheRequiredParametersWasNotPassedOrIsInvalid(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 101:
            raise InvalidApplicationAPIID(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 113:
            raise InvalidUserID(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 150:
            raise InvalidTimestamp(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 200:
            raise AlbumAccessDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 201:
            raise AudioAccessDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 203:
            raise GroupAccessDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 210:
            raise AccessToWallsPostDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 211:
            raise AccessToWallsCommentDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 212:
            raise AccessToPostCommentsDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 213:
            raise AccessToStatusRepliesDenied(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 219:
            raise AdvertisementPostWasRecentlyAdded(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 220:
            raise TooManyRecipients(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 222:
            raise HyperlinksAreForbidden(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 223:
            raise TooManyReplies(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 224:
            raise TooManyAdsPosts(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 225:
            raise DonutIsDisabled(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 300:
            raise AlbumFull(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 500:
            raise ActionDeniedYouMustEnableVoiceTranslationsInTheAppSettings(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 600:
            raise NoRightsToPerformTheseOperationsWithTheAdvertisingAccount(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 603:
            raise AnErrorOccurredWhileWorkingWithTheAdvertisingAccount(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )
        elif error_code == 3102:
            raise SpecifiedLinkIsIncorrectCantFindSource(
                error_code=error_code, error_msg=error_msg, error_request_params=error_request_params
            )

        return result

    return wrapper
